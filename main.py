
def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        import basics.output.simple_message
    elif (response == "multiline_message"):
        import basics.output.simple_message


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()