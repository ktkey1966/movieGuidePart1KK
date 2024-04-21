#Kevin Key, MovieGuidePart1

#Create a function to display heading and menu choices
from re import L, M


def movie_guide():
    print('The movie guide application')
    print()
    print('Command Menu')
    print('list --> List all movies')
    print('add --> Add a movie')
    print('delete --> Delete a movie')
    print('exit --> Close the application')
    
#Use for loop to define list(movie_list)
def list(movie_list):
    for i, movie in enumerate(movie_list, start = 1):
        print(f'{i}. {movie}')
        print()
        
#Define add(movie_list) to input a variable
def add(movie_list):
    movie = input('Name: ')
    movie_list.append(movie)
    print(f'{movie} was added. \n')
    
#Define delete(movie_list) to delete a variable
def delete(movie_list):
    number = int(input('Number: '))
    if number < 1 or number > len(movie_list):
        print('Invalid movie number. \n')
    else:
        movie = movie_list.pop(number -1)
        print(f'{movie} was deleted. \n')
        
#Define main() using while loop, if and elif statements and break to exit the loop
def main():
    movie_list = ['Batman', 'Superman', 'Wonder Woman']
    
    movie_guide()
    
    while True:
        command = input('Command: ')
        if command.lower() == 'list':
            list(movie_list)
        elif command.lower() == 'add':
            add(movie_list)
        elif command.lower() == 'delete':
            delete(movie_list)
        elif command.lower() == 'exit':
            break
        else:
            print('Not a valid command, please try again. \n')
    print('Bye')
            
if __name__ == '__main__':
    main()
    
        
    


