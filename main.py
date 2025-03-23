import pygame
import country as co

class Game:
    def __init__(self):
        self.countries = {}
        self.regions = {}
        self.year = 2025
        self.turn = 1

    def next_turn(self):
        self.turn += 1
        if self.turn == 13:
            self.turn = 1
            self.year += 1
        for c in self.countries.values():
            c.resources["Food"] += 100
            c.resources["Money"] += 100
            c.resources["Reqruits"] += 1000
    def draw_map(self, screen):
        # Цвета для стран
        country_colors = {
            "Россия": (0, 200, 0),    # Зелёный
            "Франция": (0, 0, 255),   # Синий
            "Великобритания": (200, 0, 0), # Красный
            "Германия": (100, 100, 100),  # Серый
            "Украина": (255, 255, 0)   # Желтый
        }

        # Координаты регионов
        region_coords = {
            "Berlin": (100, 100, 50, 50),
            "Munich": (160, 100, 50, 50),
            "Gamburg": (100, 160, 50, 50),
            "Moscow": (400, 100, 50, 50),
            "London": (50, 40, 50, 50),
            "Kiyv": (350, 200, 50, 50),
            "Donbass": (400, 200, 50, 50),
            "Crimea": (450, 250, 50, 50),
            "Paris": (50, 150, 50, 50)
        }

        for region_name, region in self.regions.items():
            color = country_colors[region.owner.name]
            x, y, w, h = region_coords[region_name]
            pygame.draw.rect(screen, color, (x, y, w, h))
    
    def show_country_menu(self, country):
        print(f"Меню страны: {country.name}")
        print(f"Ресурсы: {country.resources}")
        print(f"Дипломатия: {country.diplomacy}")
        # Здесь можно добавить GUI для управления страной

    def show_diplomacy_menu(self, country):
        print(f"Дипломатия: {country.name}")
        print(country.diplomacy)
        # Здесь можно добавить GUI для управления дипломатией


    def handle_events(self):
        region_coords = {
            "Berlin": (100, 100, 50, 50),
            "Munich": (160, 100, 50, 50),
            "Gamburg": (100, 160, 50, 50),
            "Moscow": (400, 100, 50, 50),
            "London": (50, 200, 50, 50),
            "Kiyv": (350, 200, 50, 50),
            "Donbass": (400, 200, 50, 50),
            "Crimea": (450, 250, 50, 50),
            "Paris": (50, 100, 50, 50)
        }
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for region_name, region in self.regions.items():
                    region_rect = pygame.Rect(region_coords[region_name])
                    if region_rect.collidepoint(x, y):
                        self.show_region_menu(region)  # Показываем меню региона
        return True

    def show_region_menu(self, region):
        print(f"Меню региона: {region.name}, Владелец: {region.owner.name}")
        # Здесь можно добавить GUI для управления регионом
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        # Игровой цикл
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.next_turn()
            screen.fill((0, 0, 127))  # Очищаем экран синим цветом
            self.draw_map(screen)
            pygame.display.flip()
        pygame.quit()
    def declareWar(c1, c2):
        if c1 in c2.diplomacy["War"] and c2 in c1.diplomacy["War"]:
            return
        c1.diplomacy["War"].append(c2)
        c2.diplomacy["War"].append(c1)
    def peace(c1, c2):
        if not(c1 in c2.diplomacy["War"] and c2 in c1.diplomacy["War"]):
            return
        c1.diplomacy["War"].remove(c2)
        c2.diplomacy["War"]. remove(c1)

if __name__ == "__main__":
    game = Game()
    
    rus = co.Country("Россия", {"Food": 10000, "Money": 1000, "Reqruits": 100000})
    fr = co.Country("Франция", {"Food": 1000, "Money": 1056, "Reqruits": 1000})
    uk = co.Country("Великобритания", {"Food": 1000, "Money": 1100, "Reqruits": 1000})
    germ = co.Country("Германия", {"Food": 1000, "Money": 1100, "Reqruits": 1000})
    ukr = co.Country("Украина", {"Food": 10, "Money": 110000000, "Reqruits": 10})
    
    rus.diplomacy = {"War": [ukr], "Union": [], "Toys": []}
    ukr.diplomacy = {"War": [rus], "Union": [germ, uk, fr], "Toys": []}
    fr.diplomacy = {"War": [], "Union": [germ, uk, ukr], "Toys": []}
    uk.diplomacy = {"War": [], "Union": [germ, fr, ukr], "Toys": []}
    germ.diplomacy = {"War": [], "Union": [fr, uk, ukr], "Toys": []}
    
    regions = {"Berlin": co.Region("Berlin", germ), "Munich": co.Region("Munich", germ), "Gamburg": co.Region("Gamburg", germ), "Moscow": co.Region("Moscow", rus), "London": co.Region("London", uk), "Kiyv": co.Region("Kiyv", ukr), "Donbass": co.Region("Donbass", rus), "Crimea": co.Region("Crimea", rus), "Paris": co.Region("Paris", fr)}
    
    game.countries = {"Russia": rus, "France": fr, "UK": uk, "Germany": germ, "Ukraine": ukr}
    game.regions = regions
    game.run()