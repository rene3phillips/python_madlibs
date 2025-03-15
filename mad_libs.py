while True:

    # Python Mad Libs Warm-Up Activity
    # Welcome message
    print("\nWelcome to Python Mad Libs!")
    print("Answer the following questions to create your very own silly story.\n")
    # Gather user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    # Build the story using an f-string
    story = (
        f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
        "I couldn't believe my eyes!"
    )
    # Display the completed story
    print("\nHere is your story:")
    print(story)

    # Save Story to a Text File
    save_story = input("\nWould you like to save your story to a text file? (yes/no) ").lower().strip()
    if save_story == "yes":
        file_name = input("What would you like to name your file? ")
        with open(f"{file_name}.txt", "w") as file:
            file.write(story)
        print(f"Your story has been saved to '{file_name}.txt'.")
    else:
        pass
    
    # Replay Feature
    play_again = input("\nWould you like to play again? (yes/no) ").lower().strip()
    if play_again == "yes":
        continue
    else:
        print("Thank you for playing!\n")
        break 