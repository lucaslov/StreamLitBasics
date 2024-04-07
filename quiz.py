import streamlit as st

def main():
    st.title("Software Engineering Quiz")

    # Define questions and options
    questions = [
        "What does 'DRY' stand for in software engineering?",
        "What is the difference between 'git merge' and 'git rebase'?",
        "What is the purpose of unit testing in software development?",
        "What is an API?"
    ]
    options = [
        ["Do Repeat Yourself",
         "Data Retention Yield", 
         "Deploy Refactor Yield", 
         "Don't Repeat Yourself"],
        ["git merge and git rebase are the same.",
         "git merge combines changes from different branches, while git rebase integrates changes by moving the entire feature branch on top of the base branch.",
         "git merge undoes changes made in the current branch.",
         "git rebase is used to merge branches without conflicts."],
        ["To test individual units or components of a software to ensure they function correctly in isolation.",
         "To test the software as a whole to ensure it meets the requirements.",
         "To test the software for performance issues only.",
         "Unit testing is not necessary in software development."],
        ["Application Processing Interface", 
         "Automated Program Integration", 
         "Application Programming Interface", 
         "Automated Programming Interface"]
    ]
    answers = [3, 1, 0, 2]  # Index of the correct option for each question

    # Display questions and collect user answers
    user_answers = []
    for i, question in enumerate(questions):
        user_answer = st.radio(f"Question {i+1}: {question}", options[i], index=None)
        user_answers.append(user_answer)

    # Display feedback after submission
    if st.button("Submit"):
        st.title("Feedback")
        correct_answers = 0
        for i, user_answer in enumerate(user_answers):
            correct_option = options[i][answers[i]]
            st.subheader(f"Question {i+1}:")
            if user_answer == correct_option:
                st.write("Your answer is correct!")
                correct_answers += 1
            else:
                st.write(f"Sorry, the correct answer is {correct_option}.")

        # Display final score
        st.title("Quiz Result")
        st.write(f"You got {correct_answers} out of {len(questions)} questions correct.")

    # Clear button to hide feedback and clear inputs
    if st.button("Clear"):
        st.title("Software Engineering Quiz")
        user_answers.clear()

if __name__ == "__main__":
    main()
