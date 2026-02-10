from random import choice, randint

edged_weapons = [
    "Espada Longa", "Espada Curta", "Cimitarra", "Katana", "Adaga",
    "Foice", "Machadinha", "Sabre", "Espada Bastarda"
]
impact_weapons = [
    "Martelo de guerra", "Maça", "Clava", "Mangual", "Tacape",
    "Cajado", "Marreta", "Mangual Pesado", "Maça Estrelada", "Porrete"
]
piercing_weapons = [
    "Lança", "Rapieira", "Florete", "Tridente", "Pique",
    "Adaga Perfurante", "Estoque", "Arpão", "Faca"
]
ranged_weapons = [
    "Arco", "Arco Longo", "Arco de Guerra", "Besta", "Besta pesada",
    "Arpão de Arremesso"
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
    "Manuscrito Antigo",
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
    "Máscara Espiritual",
    "Totem de Mana",
    "Pingente Místico"
]
gear_equipments = [
    "Luvas de Couro",
    "Botas Reforçadas",
    "Bracelete de Ferro",
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
all_weapons = edged_weapons + impact_weapons + piercing_weapons
all_obj = religious_obj + study_obj + common_obj + mystic_obj + gear_equipments
all_equipments = armors_equipments + shields_equipments
all_items = all_weapons + all_obj + all_equipments

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

damages = ["1d6", "2d4", "1d8", "2d6", "1d10", "3d4", "2d8", "3d6", "2d10"]

itemQtd = 5

def generate_itens(itemQtd):
    item_list = []

    for item in range(itemQtd):
        selected_type, selected_god = choice(all_items), choice(gods_names)
        
        damage_type = ""

        if selected_type in edged_weapons:
            damage_type = "cortante"
        elif selected_type in impact_weapons:
            damage_type = "de impacto"
        else:
            damage_type = "perfurante"
        itemDict = {
            "itemType": selected_type,
            "itemName": f"{selected_type} de {selected_god}"
        }
        if itemDict["itemType"] in all_weapons:
            itemDict["itemDescription"] = f"{choice(damages)} de dano {damage_type}"
        elif itemDict["itemType"] in all_obj:
            itemDict["itemDescription"] = f"+{randint(4, 16)} em {choice(skills_names)}"
        else:
            itemDict["itemDescription"] = f"+{randint(4, 16)} de Defesa"
        item_list.append({
        "name": itemDict["itemName"],
        "description": itemDict["itemDescription"]
        })
    return item_list