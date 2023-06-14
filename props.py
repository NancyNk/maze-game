class Props:
    def __init__(self):
        self._rows =  0
        self._cols =  0
        self._start = (0,0)
        self._goal =  (0,0)
        self._invalid_count = 0
        self._invalid_positions = set()
        self._invalid_chars = ["X","x","#", "-", "|", "+", "*"]
    def __str__(self): #parsing the props of the maze
        return f"Rows: {self._rows}\nCols: {self._cols}\nStart: {self._start}\nGoal: {self._goal}\nInvalid Count: {self._invalid_count}\nInvalid Positions: {self._invalid_positions}\nInvalid Chars: {self._invalid_chars}"
        # Return the properties of the generated maze
    def __iadd__(self, invalid_count):
        self._invalid_count += invalid_count

    @staticmethod
    def compare (maze, other) -> bool:# used to compare the invalid positions in the first maze with the second maze in order to sort them in accorsing to the diffuclity odf the maze
        return maze.invalid_count > other.invalid_count
    @property #Getter method
    def rows(self):
        return self._rows
    @rows.setter
    def rows(self, rows):
        self._rows = rows
    @property
    def cols(self):
        return self._cols
    @cols.setter
    def cols(self, cols):
        self._cols = cols
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, start):
        self._start = start
    @property
    def goal(self):
        return self._goal
    @goal.setter
    def goal(self, goal):
        self._goal = goal
    @property
    def invalid_count(self):
        return self._invalid_count
    @invalid_count.setter
    def invalid_count(self, invalid_count):
        self._invalid_count = invalid_count
    @property
    def invalid_positions(self):
        return self._invalid_positions
    @invalid_positions.setter
    def invalid_positions(self, invalid_positions):
        self._invalid_positions = invalid_positions
    def add_invalid_position(self, invalid_position):
        self._invalid_positions += invalid_position
    @property
    def invalid_chars(self):
        return self._invalid_chars
    @invalid_chars.setter
    def add_invalid_char(self, invalid_char):
        self._invalid_chars.append(invalid_char)
