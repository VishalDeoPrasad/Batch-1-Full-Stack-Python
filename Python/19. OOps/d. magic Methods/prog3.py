class Score:
    def __init__(self, marks):
        self.marks = marks

    def __len__(self):
        return len(self.marks)
    
    def __getitem__(self, idx):
        return self.marks[idx]
    
s = Score([99, 86, 45, 33, 87])
print(s[3])
print(len(s))