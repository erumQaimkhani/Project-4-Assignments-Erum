# Description: This file contains the visual representation of the hangman game.
# The lives_visual_dict dictionary contains the ASCII art for the hangman at different stages of the game.
lives_visual_dict = {
    0: """
        ___________
       | /        | 
       |/        ( )
       |         /|\\
       |         / \\
       |
    """,
    1: """
        ___________
       | /        | 
       |/        ( )
       |         /|\\
       |         / 
       |
    """,
    2: """
        ___________
       | /        | 
       |/        ( )
       |         /|\\
       |          
       |
    """,
    3: """
        ___________
       | /        | 
       |/        ( )
       |         /|
       |          
       |
    """,
    4: """
        ___________
       | /        | 
       |/        ( )
       |          |
       |          
       |
    """,
    5: """
        ___________
       | /        | 
       |/        ( )
       |          
       |          
       |
    """,
    6: """
        ___________
       | /        | 
       |/        
       |          
       |          
       |
    """,
    7: """
        ___________
       | /        
       |/        
       |          
       |          
       |
    """,
    8: """
        ___________
       |          
       |          
       |          
       |          
       |
    """,
    9: """
       |
       |
       |
       |
       |
    """,
    10: ""
}
