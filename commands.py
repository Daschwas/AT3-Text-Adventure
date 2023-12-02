def end_game(player, backpack):
    has_camera = backpack.in_backpack("Camera") != -1
    has_watch = backpack.in_backpack("Stylish Watch") != -1
    has_loan = backpack.in_backpack("Loan Document") != -1
    has_fraud = backpack.in_backpack("Loan Document with Fake Name") != -1

    print("As the clock strikes 5:00 PM, you find yourself at the exit of the bustling shopping mall.")

    if has_camera and not has_loan:
        print("Congratulations! You successfully navigated the maze of shops, capturing vibrant and memorable moments "
              "with your new camera.")
        print("The snapshots of laughter, dazzling storefronts, and unexpected encounters will be cherished forever.")
        print("It's been a successful and enjoyable shopping adventure!")
    elif has_watch and not has_loan:
        print("You glance at your new stylish watch and realize you spent the day strolling through the mall, "
              "enjoying its ambiance.")
        print("Not only did you get the item of your desire, the experience itself was also worth every moment.")
        print("You leave the mall with a sense of contentment.")
    else:
        print("Unfortunately, your shopping spree didn't go as planned and you leave largely empty-handed.")
        print("Better luck next time!")
        player.game_over = True

    if has_fraud:
        print("You breathe a sigh of relief as you realise you narrowly escaped taking on a heavy loan by using a "
              "fake name.")
        print("It's a reminder to be cautious and honest in financial dealings. Dodging that bullet was a close call!")

    if has_camera and has_loan:
        print("Despite the joy of capturing moments with your new camera, you can't shake the uneasy feeling of having "
              "a signed loan document in your backpack.")
        print("The terms look challenging, and the weight of potential debt lingers. It's a lesson learned about the "
              "importance of financial responsibility.")
        player.game_over = True
    elif has_camera and has_loan:
        print("You weigh the pros and cons of your purchases. The camera brought joy, but the signed loan document "
              "brings a sense of responsibility.")
        print("The terms look challenging, and the weight of potential debt lingers. It's a lesson learned about the "
              "importance of financial responsibility.")
        player.game_over = True
    elif has_loan:
        print("You exit the mall with a signed loan document in your backpack. The terms look challenging.")
        print("Hopefully, you can manage the repayments. It's a reminder to be cautious about what you agree to.")
        player.game_over = True

    if not player.game_over:
        print("You win! Your shopping adventure was huge success!")
        player.game_over = True
    else:
        print(
            "Game Over! Whether it was the maze-like layout or unexpected challenges, this shopping trip didn't go as "
            "planned.")
        print("Better luck next time! The mall is always open for new adventures.")
