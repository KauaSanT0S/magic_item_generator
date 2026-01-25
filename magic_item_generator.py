from random import *
from os import system, name

edged_weapons = [
    "Espada Longa", "Espada Curta", "Cimitarra", "Katana", "Adaga",
    "Foice", "Machadinha", "Sabre", "Espada Bastarda"
]
impact_weapons = [
    "Martelo de guerra", "Maça", "Clava", "Mangual", "Tacape",
    "Cajado", "Marreta", "Mangual Pesado", "Maça Estrelada", "Porrete"
]
piercing_weapons = [
    "Lança", "Rapieira", "Florete", "Tridente", "Pique"
    "Adaga Perfurante", "Estoque", "Arpão", "Faca"
]
ranged_weapons = [
    "Arco", "Arco Longo", "Arco de Guerra", "Besta", "Besta pesada",
    "Funda", "Arpão de Arremesso", "Bumerangue"
]

religious_obj = [
    "Rosário de Ossos",
    "Tocha Eterna",
    "Cálice Sagrado",
    "Anel de Devoção",
    "Livro de Preces",
    "Manto Cerimonial",
    "Incenso Antigo",
    "Sino Ritualístico",
    "Relíquia Divina",
    "Estátua Votiva",
]
study_obj = [
    "Livro de Anotações",
    "Mapa Astral",
    "Pena de Corvo",
    "Globo de Navegação",
    "Manuscrito Antigo"
    "Tinta de Registro",
    "Diário de Campo",
]
common_obj = [
    "Colar de Jóias",
    "Anel Dourado",
    "Diário de Viagem",
    "Cordão de Couro",
    "Moeda de Prata",
    "Fita de Cabelo",
    "Medalhão Velho",
    "Cantil de Metal",
    "Tecido Bordado",
    "Espelho de Bolso"
]
mystic_obj = [
    "Cristal Pulsante",
    "Orbe Translúcido",
    "Foco de Energia",
    "Coroa Espectral",
    "Vela Negra",
    "Pedra Rúnica",
    "Selo Encantado",
    "Másara Espiritual",
    "Totem de Mana",
    "Pingente Místico"
]
gear_equipments = [
    "Luvas de Couro",
    "Botas Reforçadas",
    "Bracelete de Ferro"
    "Colar Protetor",
    "Anel de Energia",
    "Capa Leve",
    "Ombreira de Aço",
    "Elmo de Viajante",
    "Broche Velho"
]
armors_equipments = [
    "Armadura de Escamas",
    "Armadura de Couro",
    "Armadura de Guerra",
    "Armadura de Caçador",
    "Peitoral Cerimonial",
    "Cota de Anéis",
    "Cota Revestida",
    "Túnica de Combate",
    "Couraça de Titânio",
    "Manto Reforçado",
]
shields_equipments = [
    "Escudo Reforçado",
    "Escudo Elemental",
    "Escudo Cerimonial",
    "Escudo de Guerra",
    "Escudo de Ferro",
    "Escudo de Vigília",
    "Escudo de Batalha",
    "Escudo de Impacto",
    "Escudo do Vigia",
    "Escudo do Guardião"
]
all_weapons = edged_weapons + impact_weapons + piercing_weapons + ranged_weapons
all_obj = religious_obj + study_obj + common_obj + mystic_obj + gear_equipments
all_equipments = armors_equipments + shields_equipments

gods_names = [
    "Aharadak", "Allihanna", "Arsenal", "Azgher", "Hyninn",
    "Kallyadranoch", "Khalmyr", "Lena", "Lin-Wu", "Marah",
    "Megalokk", "Nimb", "Oceano", "Sszaas", "Tanna-Toh",
    "Tenebra", "Thwor", "Thyatis", "Valkaria", "Wynna"
]
skills_names = [
    "Acrobacia", "Adestramento", "Atletismo",
    "Atuação", "Conhecimento", "Cura",
    "Diplomacia", "Enganação", "Fortitude",
    "Furtividade", "Iniciativa", "Intimidação",
    "Intuição", "Investigação", "Ladinagem",
    "Luta", "Misticismo", "Nobreza",
    "Percepção", "Pontaria", "Reflexos",
    "Religião", "Sobrevivência", "Vontade"
]

damages_rank1 = ["1d6", "2d4", "1d8"]
damages_rank2 = ["2d6", "1d10", "3d4"]
damages_rank3 = ["2d8", "3d6", "2d10"]

def cls():
    system('cls' if name == 'nt' else 'clear')

def generate_itens():
    run_again = 1
    while run_again == 1:
        cls()
        item_list = []

        type_selection = int(input("Selecione um tipo de objeto:\n1 - Arma\n2 - Objeto\n3 - Armadura\n\n"))
        cls()
        quantity_selection = int(input("Selecione uma quantidade de itens: \n\n"))
        cls()
        rank_selection = int(input("Selecione um Rank\n1 - Rank 1\n2 - Rank 2\n3 - Rank 3\n\n"))
        cls()

        for i in range(quantity_selection):
            item_god_name = choice(gods_names)

            if rank_selection == 1:
                item_bonus = randint(2, 6)
            elif rank_selection == 2:
                item_bonus = randint(7, 11)
            else:
                item_bonus = randint(12, 16)
            if type_selection == 1:
                item_type = choice(all_weapons)
                if item_type in edged_weapons:
                    damage_type = "cortante"
                elif item_type in impact_weapons:
                    damage_type = "impactante"
                else:
                    damage_type = "perfurante"
                if rank_selection == 1:
                    item_damage = choice(damages_rank1)
                if rank_selection == 2:
                    item_damage = choice(damages_rank2)
                else:
                    item_damage = choice(damages_rank3)
                item_name = f"- {item_type} de {item_god_name}: {item_damage} de dano {damage_type}."

            elif type_selection == 2:
                item_type = choice(all_obj)
                item_skill = choice(skills_names)
                item_name = f"- {item_name} de {item_god_name}: +{item_bonus} em {item_skill}."

            else:
                item_type = choice(all_equipments)
                item_name = f"- {item_type} de {item_god_name}: +{item_bonus}"
            
            print(f"{item_name}\n")
            item_list.append(item_name)
        run_again = int(input("\nDeseja continuar?\n1 - Sim\n2 - Não\n"))
        cls()
    
    return item_list