import os
import time
import random
import json

class FarmSimulator:
    def __init__(self):

        print("🔁 Carregando progresso...")
        self.load_progress()
        time.sleep(2)
        self.clear_console()

        if not hasattr(self, 'farm_name') or not self.farm_name:
            self.farm_name = input("🌾 Digite o nome da sua fazenda: ")

        self.money = 100
        self.seeds = {"01": {"name": "🌽 Milho", "quantity": 2}, "02": {"name": "🌾 Trigo", "quantity": 0}, "03": {"name": "🌱 Soja", "quantity": 0}}
        self.crops = []
        self.silo = {"Milho": 0, "Trigo": 0, "Soja": 0}
        self.prices = {"Milho": 5, "Trigo": 4, "Soja": 6}  # Preços iniciais
        self.day = 1

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause_and_clear(self, message):
        print(message)
        time.sleep(3)
        self.clear_console()

    def display_status(self):
        self.clear_console()
        print(f"\n🌾===== Fazenda {self.farm_name} =====🌾")  # Exibe o nome da fazenda
        print(f"🌞 Dia: {self.day}")
        print(f"💰 Dinheiro: ${self.money}")
        print("🌱 Sementes:")
        for seed_id, seed_info in self.seeds.items():
            print(f"  {seed_id} {seed_info['name']} - {seed_info['quantity']} sementes")
        print("\n🌾=== Plantações ===🌾")
        if self.crops:
            for crop in self.crops:
                state = "🍂 Pronto para colheita" if crop["days_left"] <= 0 else f"{crop['days_left']} dias restantes"
                print(f"  {crop['type']} - {state}")
        else:
            print("🌱  Nenhuma plantação 🌱")
        print("\n📉=== Preços do mercado ===📉")
        for crop, price in self.prices.items():
            print(f"  {crop}: ${price} por unidade")
        print("===================\n")

    def plant_seeds(self):
        self.clear_console()
        print("\n🌱===== PLANTAR =====🌱")
        print("Tipos de sementes disponíveis:")
        for seed_id, seed_info in self.seeds.items():
            print(f"  {seed_id} {seed_info['name']} - {seed_info['quantity']} sementes")

        crop_id = input("Escolha o ID da semente para plantar: ")
        if crop_id not in self.seeds or self.seeds[crop_id]['quantity'] <= 0:
            self.pause_and_clear("🚫 ID inválido ou sementes insuficientes.")
            return

        try:
            quantity = int(input(f"Quantas sementes de {self.seeds[crop_id]['name']} você quer plantar? "))
            if quantity <= 0 or quantity > self.seeds[crop_id]['quantity']:
                self.pause_and_clear("🚫 Quantidade inválida.")
                return

            for _ in range(quantity):
                crop_days = random.randint(3, 5)
                self.crops.append({"type": self.seeds[crop_id]['name'], "days_left": crop_days})

            self.seeds[crop_id]['quantity'] -= quantity
            self.pause_and_clear(f"🌱 Você plantou {quantity} {self.seeds[crop_id]['name']}(s).")
        except ValueError:
            self.pause_and_clear("⚠️ Por favor, insira um número válido.")

    def harvest_crops(self):
        self.clear_console()
        harvested = {}
        for crop in self.crops[:]:
            if crop["days_left"] <= 0:
                crop_type = crop["type"]
                harvested[crop_type] = harvested.get(crop_type, 0) + 1
                self.crops.remove(crop)

        if harvested:
            for crop_type, qty in harvested.items():
                self.silo[crop_type] += qty
            self.pause_and_clear("🌾 Você colheu as plantações prontas e enviou para o silo.")
        else:
            self.pause_and_clear("⚠️ Nenhuma plantação está pronta para ser colhida.")

    def go_to_store(self):
        self.clear_console()
        print("\n🛒===== LOJA =====🛒")
        print("1. Comprar sementes ($10 cada)")
        print("2. Voltar 🏡")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            print("🌱 Tipos de sementes disponíveis para compra:")
            for seed_id, seed_info in self.seeds.items():
                print(f"  {seed_id} {seed_info['name']}")
            crop_id = input("Escolha o ID da semente para comprar: ")

            if crop_id not in self.seeds:
                self.pause_and_clear("🚫 ID inválido.")
                return

            try:
                quantity = int(input(f"Quantas sementes de {self.seeds[crop_id]['name']} você quer comprar? "))
                cost = quantity * 10
                if quantity <= 0 or cost > self.money:
                    self.pause_and_clear("🚫 Quantidade inválida ou dinheiro insuficiente.")
                    return

                self.money -= cost
                self.seeds[crop_id]['quantity'] += quantity
                self.pause_and_clear(f"💰 Você comprou {quantity} sementes de {self.seeds[crop_id]['name']} por ${cost}.")
            except ValueError:
                self.pause_and_clear("⚠️ Por favor, insira um número válido.")
        elif choice == "2":
            return
        else:
            self.pause_and_clear("🚫 Opção inválida.")

    def sell_crops(self):
        self.clear_console()
        print("\n💸===== VENDA DE GRÃOS =====💸")
        print("Grãos disponíveis no silo:")
        for crop, qty in self.silo.items():
            print(f"  {crop}: {qty} unidades - ${self.prices[crop]} cada")
        crop_to_sell = input("Escolha o tipo de grão para vender: ")

        if crop_to_sell not in self.silo or self.silo[crop_to_sell] <= 0:
            self.pause_and_clear("🚫 Grão inválido ou quantidade insuficiente.")
            return

        try:
            quantity = int(input(f"Quantas unidades de {crop_to_sell} você quer vender? "))
            if quantity <= 0 or quantity > self.silo[crop_to_sell]:
                self.pause_and_clear("🚫 Quantidade inválida.")
                return

            earnings = quantity * self.prices[crop_to_sell]
            self.money += earnings
            self.silo[crop_to_sell] -= quantity
            self.pause_and_clear(f"💰 Você vendeu {quantity} unidades de {crop_to_sell} por ${earnings}.")
        except ValueError:
            self.pause_and_clear("⚠️ Por favor, insira um número válido.")

    def advance_day(self):
        self.clear_console()
        self.day += 1
        for crop in self.crops:
            crop["days_left"] -= 1
        self.update_prices()
        self.pause_and_clear("🌅 Avançando para o próximo dia...")

    def update_prices(self):
        for crop in self.prices:
            self.prices[crop] = random.randint(3, 8)  # Define preços aleatórios entre 3 e 8

    def view_silo(self):
        self.clear_console()
        print("\n🚜===== SILO =====🚜")
        print("Grãos no silo:")
        for crop, qty in self.silo.items():
            print(f"  {crop}: {qty} unidades")
        self.pause_and_clear("🔙 Voltar para o menu principal.")

    def save_progress(self):
        appdata_path = os.getenv('APPDATA')
        if appdata_path:
            file_path = os.path.join(appdata_path, "texasfarm.json")
            data = {
                "farm_name": self.farm_name,
                "money": self.money,
                "seeds": self.seeds,
                "crops": self.crops,
                "silo": self.silo,
                "prices": self.prices,
                "day": self.day
            }
            with open(file_path, "w") as f:
                json.dump(data, f)
            print("📝 Progresso salvo com sucesso!")

    def load_progress(self):
        appdata_path = os.getenv('APPDATA')
        if appdata_path:
            file_path = os.path.join(appdata_path, "texasfarm.json")
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    data = json.load(f)
                    self.farm_name = data["farm_name"]
                    self.money = data["money"]
                    self.seeds = data["seeds"]
                    self.crops = data["crops"]
                    self.silo = data["silo"]
                    self.prices = data["prices"]
                    self.day = data["day"]

    def main_menu(self):
        while True:
            self.display_status()
            print("1. Plantar sementes")
            print("2. Colher plantações")
            print("3. Ir à loja")
            print("4. Vender grãos")
            print("5. Ver silo")
            print("6. Avançar para o próximo dia")
            print("7. Salvar progresso")
            print("8. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.plant_seeds()
            elif choice == "2":
                self.harvest_crops()
            elif choice == "3":
                self.go_to_store()
            elif choice == "4":
                self.sell_crops()
            elif choice == "5":
                self.view_silo()
            elif choice == "6":
                self.advance_day()
            elif choice == "7":
                self.save_progress()
            elif choice == "8":
                self.save_progress()
                print("🚪 Saindo... Até logo!")
                break
            else:
                self.pause_and_clear("🚫 Opção inválida.")

if __name__ == "__main__":
    simulator = FarmSimulator()
    simulator.main_menu()
