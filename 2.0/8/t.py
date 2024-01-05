class RedButton:
    def __init__(self) -> None:
        self.cnt = 0

    def click(self) -> str:
        self.cnt += 1
        return "Тревога!"
    
    def count(self) -> int:
        return self.cnt

first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
