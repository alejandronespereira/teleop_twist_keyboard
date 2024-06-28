import yaml


class KeyMapper:

    def __init__(self, mappings_file):
        self._mappings_file = mappings_file

        # Declare default lexical mappings
        self._key_mappings = {
            'speed_up': 'q',
            'speed_down': 'z',
            'linear_speed_up': 'w',
            'linear_speed_down': 'x',
            'angular_speed_up': 'e',
            'angular_speed_down': 'c',
            'forward': 'i',
            'forward_right': 'o',
            'turn_left': 'j',
            'turn_right': 'l',
            'forward_left': 'u',
            'backward': ',',
            'backward_right': '.',
            'backward_left': 'm',
            'forward_right_strafe': 'O',
            'forward_strafe': 'I',
            'strafe_left': 'J',
            'strafe_right': 'L',
            'forward_left_strafe': 'U',
            'backward_strafe': '<',
            'backward_right_strafe': '>',
            'backward_left_strafe': 'M',
            'up': 't',
            'down': 'b'
        }

        self.read_keymapping(mappings_file)

        self.create_bindings()

    def create_bindings(self):
        self._move_bindings = {
            self._key_mappings['forward']: (1, 0, 0, 0),
            self._key_mappings['forward_right']: (1, 0, 0, -1),
            self._key_mappings['turn_left']: (0, 0, 0, 1),
            self._key_mappings['turn_right']: (0, 0, 0, -1),
            self._key_mappings['forward_left']: (1, 0, 0, 1),
            self._key_mappings['backward']: (-1, 0, 0, 0),
            self._key_mappings['backward_right']: (-1, 0, 0, 1),
            self._key_mappings['backward_left']: (-1, 0, 0, -1),
            self._key_mappings['forward_right_strafe']: (1, -1, 0, 0),
            self._key_mappings['forward_strafe']: (1, 0, 0, 0),
            self._key_mappings['strafe_left']: (0, 1, 0, 0),
            self._key_mappings['strafe_right']: (0, -1, 0, 0),
            self._key_mappings['forward_left_strafe']: (1, 1, 0, 0),
            self._key_mappings['backward_strafe']: (-1, 0, 0, 0),
            self._key_mappings['backward_right_strafe']: (-1, -1, 0, 0),
            self._key_mappings['backward_left_strafe']: (-1, 1, 0, 0),
            self._key_mappings['up']: (0, 0, 1, 0),
            self._key_mappings['down']: (0, 0, -1, 0),
        }

        self._speed_bindings = {
            self._key_mappings['speed_up']: (1.1, 1.1),
            self._key_mappings['speed_down']: (.9, .9),
            self._key_mappings['linear_speed_up']: (1.1, 1),
            self._key_mappings['linear_speed_down']: (.9, 1),
            self._key_mappings['angular_speed_up']: (1, 1.1),
            self._key_mappings['angular_speed_down']: (1, .9),
        }

    def read_keymapping(self, file):
        ''' Read the mappings from a yaml file.'''

        if file is None:
            return

        with open(file, 'r') as f:
            config = yaml.safe_load(f)

        # Check there are not repeated values
        if len(list(config.values())) != len(set(config.values())):
            raise RuntimeError("Repeated keys in the yaml file.")

        self._key_mappings.update(config)

        # Check the new mappings don't have repeated values
        if len(list(self._key_mappings.values())) != len(set(self._key_mappings.values())):
            raise RuntimeError("Repeated elements in the mappings.")

    def speed_bindings(self):
        return self._speed_bindings

    def move_bindings(self):
        return self._move_bindings

    def msg(self):
        return (
            '---------------------------\n'
            'Moving around:\n'
            f'{self._key_mappings["forward_left"]}    {self._key_mappings["forward"]}    {self._key_mappings["forward_right"]}\n'
            f'{self._key_mappings["turn_left"]}         {self._key_mappings["turn_right"]}\n'
            f'{self._key_mappings["backward_left"]}    {self._key_mappings["backward"]}    {self._key_mappings["backward_right"]}\n'
            '\n'
            'For Holonomic mode (strafing), hold down the shift key:\n'
            '---------------------------\n'
            f'{self._key_mappings["forward_left_strafe"]}    {self._key_mappings["forward_strafe"]}    {self._key_mappings["forward_right_strafe"]}\n'
            f'{self._key_mappings["strafe_left"]}         {self._key_mappings["strafe_right"]}\n'
            f'{self._key_mappings["backward_left_strafe"]}    {self._key_mappings["backward_strafe"]}    {self._key_mappings["backward_right_strafe"]}\n'
            '\n'
            f'{self._key_mappings["up"]} : up (+z)\n'
            f'{self._key_mappings["down"]} : down (-z)\n'
            '\n'
            'anything else : stop\n'
            '\n'
            f'{self._key_mappings["speed_up"]}/{self._key_mappings["speed_down"]} : increase/decrease max speeds by 10%\n'
            f'{self._key_mappings["linear_speed_up"]}/{self._key_mappings["linear_speed_down"]} : increase/decrease only linear speed by 10%\n'
            f'{self._key_mappings["angular_speed_up"]}/{self._key_mappings["angular_speed_down"]} : increase/decrease only angular speed by 10%\n'
            '\n'
            'CTRL-C to quit\n')
