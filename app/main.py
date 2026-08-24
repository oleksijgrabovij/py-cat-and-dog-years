def get_human_age(cat_age: int, dog_age: int) -> list:
    def calculate_human_years(animal_age: int,
                              years_per_human_year: int) -> int:
        if animal_age < 15:
            return 0
        elif animal_age < 24:
            return 1
        else:
            return 2 + (animal_age - 24) // years_per_human_year

    cat_human_age = calculate_human_years(cat_age, 4)
    dog_human_age = calculate_human_years(dog_age, 5)

    return [cat_human_age, dog_human_age]
