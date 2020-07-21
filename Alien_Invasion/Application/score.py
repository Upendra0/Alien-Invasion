def update(score):
    """
    Update the score if it is greater than previous best score
    """
    score=int(score)
    with open("E:\Alien_Invasion\Application\\best_score.txt", 'r') as fr:
        data=int(fr.read())
        if data<score:
            with open("E:\Alien_Invasion\Application\\best_score.txt", 'w') as fw:
                fw.write(str(score))
