class Pokémon :
    #defining class variables
    name = ''
    level = 0
    elementType = 'normal'
    maximum_health = 0
    current_health = maximum_health
    isAlive = True

    def __init__(self, name, level, elementType) : #whos that pokemon
        #assigning values to variables
        self.name = name
        self.level = level
        self.type = elementType.lower()
        self.maximum_health = self.level
        self.current_health = self.maximum_health
    def __repr__ (self) :
        return '{} the Pokémon'.format(self.name)
    
    def lose_health (self, damage) :
        self.current_health -= damage
        if self.current_health > 0 :
            print('{name} is now at {health} health!'.format(name=self.name,health=self.current_health))
        else : 
            self.knock_out()
    def knock_out (self) :
        self.isAlive = False
        print('{} has fallen!'.format(self.name))

    def gain_health (self) :
        print('{name} is now at {health} health!'.format(name=self.name,health=self.current_health))

    def knock_out (self) :
        self.current_health = 0
        self.isAlive = False

    # basic opposite types
    weaknesses = {'fire' : 'water', 'water' : 'grass', 'grass' : 'fire'}

    #checks to see if an item is of pokemon class
    def isPokemon (self, alternate_pokemon) :
        if not type(alternate_pokemon) == Pokémon :
            raise NotPokémon
    
    #defines effectiveness of oppononents attacks
    def compare_types (self, alternate_pokemon) :
        self.isPokemon(alternate_pokemon)
        
        enemy_type = alternate_pokemon.type
        self_type = self.type
        if self_type == enemy_type : #same type
            self.attackPower = self.level
        elif self.weaknesses[self_type] == enemy_type : #opponent is stronger type
            self.attackPower =  0.5 * self.level 
        elif alternate_pokemon.weaknesses[enemy_type] == self_type : #opponent is weaker type
            self.attackPower = 2.0 * self.level
        else : # unrecognized type or whatever
            self.attackPower == self.level

    # attacks and deals damage
    def attack (self, alternate_pokemon) :
        self.isPokemon(alternate_pokemon)
        self.compare_types(alternate_pokemon)
        if self.current_health > 0 and alternate_pokemon.current_health > 0 :
            alternate_pokemon.lose_health(self.attackPower)
        elif alternate_pokemon.current_health <= 0 :
            alternate_pokemon.knock_out()
        
class Trainer :
    name = ''
    potions = 0
    potion_value = 20
    pokemans = []
    active_pokemon = Pokémon()
    def __init__(self, name, potions, pokemans) :
        self.name = name
        self.potions = potions
        self.pokemans = pokemans
        self.active_pokemon = pokemans[0]

    def __repr__(self) :
        return 'This is {} the trainer!'.format(self.name)

    def can_battle(self) :
        for pokemon in self.pokemans :
            if pokemon.isAlive :
                return True
        return False
    
    # uses potion
    def use_potion (self, pokemon) :
        potions -= 1
        pokemon.current_health += self.potion_value
        if pokemon.current_health > pokemon.maximum_health :
            pokemon.current_health = pokemon.maximum_health
        print ('{} used a potion! {}\'s health is now {}'.format(self.name, pokemon.name, pokemon.current_health))
        
    def switch_pokemon (self) :
        for pokemon in self.pokemans :
            if pokemon.isAlive :
                self.active_pokemon = pokemon
                print('{} has switch pokemon to {}!'.format(self.name, self.active_pokemon.name))
                break


        

class NotTrainer (Exception) :
    def __repr__ (self) :
        return 'This is not a trainer!'
class NotPokémon (Exception) :
    def __repr__ (self) :
        return 'That is not a Pokémon!'

# functions

def battle (player1, player2) :
    if not type(player1) == Trainer and not type(player2) == Trainer :
        raise NotTrainer
    
    while player1.can_battle() and player2.can_battle() :
        #player1 turn
        if player1.active_pokemon.current_health 
    else :
        if player1.can_battle() and not player2.can_battle() :
            return "{name} has won with {pokemon} against {opponent_name}!".format(name=player1.name, pokemon=player1.active_pokemon.name, opponent_name=player2.name)
        elif player2.can_battle() and not player1.can_battle() :
            return "{name} has won with {pokemon} against {opponent_name}!".format(name=player2.name, pokemon=player2.active_pokemon.name, opponent_name=player1.name)
        else :
            return 'Both y\'all died... Not really sure what happened to be honest.'

        
# pokemans

charmander = Pokémon('Charmander', 33, 'fire')
aquadeebus = Pokémon('Aquadeebus', 18, 'water')

ash = Trainer('Ash')