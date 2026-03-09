kickoff:
    player = receive("Enter player: ")
    # iam a comment
    goals = receive("Enter goals: ")
    referee goals >= 3:
        shout("Hat-trick!")
    assist goals == 2:
        shout("Brace!")
    offside:
        shout("Keep Training")