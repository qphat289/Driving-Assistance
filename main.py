import subprocess
import re
import pygame
import cv2
import script
import time
import threading
class SoundPlayer:
    def __init__(self, rear, crosswalk):
        pygame.mixer.init()
        self.rear_sound = pygame.mixer.Sound(rear)
        self.crosswalk_sound = pygame.mixer.Sound(crosswalk)
        self.left_pressed = False
        self.right_pressed = False
        self.brake_pressed = False
        self.last_played_time = 0

    def play_sound(self, direction):
        current_time = time.time()
        if current_time - self.last_played_time < 10:
            return

        print(f"Playing sound: {direction}")
        if direction == 'rear':
            pygame.mixer.Sound.play(self.rear_sound)
        elif direction == 'crosswalk':
            pygame.mixer.Sound.play(self.crosswalk_sound)
        self.last_played_time = current_time

class SubprocessOutputReader:
    def __init__(self, command):
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.latest_output = None
        self.speed = None  # Initialize speed attribute
        self.thread = threading.Thread(target=self._read_output)
        self.thread.start()

    def _read_output(self):
        for line in iter(self.process.stdout.readline, b''):
            output = line.decode('utf-8').strip()
            if "- INFO - " in output:
                self.latest_output = output.split("- INFO - ")[1]
                self.latest_output = self.latest_output.split('-')
                self.speed = self.extract_speed(self.latest_output)  # Extract speed from the latest output
            else:
                self.latest_output = output

    def extract_speed(self, data):
        for item in data:
            if 'speed' in item.lower():
                numbers = re.findall(r'\d+', item)
                if numbers:
                    return numbers[0]  # Return the first number found
        return None  # Return None if no speed information is found

    def get_latest_output(self):
        return self.latest_output, self.speed


def main():
    vid = cv2.VideoCapture(2)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    filename = f"{int(time.time())}.avi"
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    sound_player = SoundPlayer('resources/sounds/rear.mp3', 'resources/sounds/crosswalk.mp3')
    output_reader = SubprocessOutputReader(["dist/UI/UI.exe"])

    while True:
        ret, frame = vid.read()
        if ret:
            out.write(frame)  # Write the frame to the file
            detection = script.inference(vid)
            detection_front = script.inference_front(vid)
            output, speed = output_reader.get_latest_output()

            try:
                speed = int(speed)
            except:
                speed = None

            print(f"detection: {detection}, Last_output: {output}")

            if detection and output:
                if 'left' in detection and 'Left on' in output[0]:
                    sound_player.play_sound('rear')
                elif 'right' in detection and 'Right on' in output[0]:
                    sound_player.play_sound('rear')
                elif ('left' in detection or 'right' in detection) and 'brake(on)' in output[0]:
                    sound_player.play_sound('rear')

            if detection_front:
                if 'front' in detection_front:
                    if speed and speed > 40:
                        sound_player.play_sound('crosswalk')
        else:
            break

    # Release everything when job is finished
    vid.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
