
import datetime
import re

# ==========================================
# COLLEGE ASSISTANT AGENT
# ==========================================

# 1. KNOW THE AGENT BEING BUILT

AGENT_NAME = "College Assistant Agent"

print("=" * 50)
print(f"       WELCOME TO {AGENT_NAME.upper()}")
print("=" * 50)

# 2. KNOWLEDGE BASE
# Edit this information according to your college.

knowledge = {
    "courses": (
        "Our college offers courses such as CSE, ISE, ECE, "
        "EEE, Mechanical Engineering and Civil Engineering."
    ),

    "admission": (
        "For admission, check the college website for eligibility, "
        "application forms, entrance exams and required documents."
    ),

    "fees": (
        "College fees depend on the course and admission category. "
        "Contact the college office for the exact fee structure."
    ),

    "library": (
        "The college library provides textbooks, reference books, "
        "study materials and other academic resources."
    ),

    "exams": (
        "Check the official college or university notifications "
        "for examination timetables, hall tickets and results."
    ),

    "placements": (
        "Students can prepare for placements by learning programming, "
        "practising DSA, improving communication and solving aptitude "
        "questions."
    ),

    "timetable": (
        "Please check your department's official timetable for "
        "class timings and subject schedules."
    ),

    "attendance": (
        "Follow your university and college attendance rules. "
        "Contact your department for the minimum attendance requirement."
    ),

    "scholarship": (
        "Students can check eligible government scholarships on the "
        "National Scholarship Portal and Karnataka scholarship portals."
    ),

    "contact": (
        "For official information, contact your college office, "
        "department coordinator or faculty advisor."
    )
}

# 3. PROBLEMS / CHALLENGES
# Students may struggle to find college information quickly.
# This agent provides basic information from a knowledge base.

# 4. USER AND GOAL
# Users: Students, teachers and college applicants.
# Goal: Provide quick and simple answers to college-related questions.

# 5. USER INPUT
# The user types a question in the terminal.

# 6. TOOLS THE AGENT MAY USE
# Tool 1: Knowledge-base search
# Tool 2: Date and time
# Tool 3: Calculator
# Tool 4: Study tips generator


def search_knowledge(question):
    """Find information related to the user's question."""

    question = question.lower()

    keywords = {
        "courses": ["course", "courses", "branch", "branches", "department"],
        "admission": ["admission", "apply", "application", "eligibility"],
        "fees": ["fee", "fees", "payment", "tuition"],
        "library": ["library", "book", "books"],
        "exams": ["exam", "exams", "result", "hall ticket"],
        "placements": ["placement", "placements", "job", "career", "interview"],
        "timetable": ["timetable", "time table", "class schedule"],
        "attendance": ["attendance", "absent", "present"],
        "scholarship": ["scholarship", "financial aid"],
        "contact": ["contact", "office", "coordinator", "faculty"]
    }

    for topic, words in keywords.items():
        if any(word in question for word in words):
            return knowledge[topic]

    return None


def get_date_time():
    """Tool: Return the current date and time."""

    now = datetime.datetime.now()

    return (
        f"Today's date is {now.strftime('%d-%m-%Y')} "
        f"and the current time is {now.strftime('%I:%M %p')}."
    )


def calculate(expression):
    """Tool: Calculate simple mathematical expressions safely."""

    expression = expression.strip()

    # Allow only numbers and basic arithmetic operators.
    if not re.fullmatch(r"[0-9+\-*/(). %]+", expression):
        return "Please enter a valid mathematical expression."

    try:
        # No built-in functions or variables are available.
        result = eval(expression, {"__builtins__": {}}, {})

        return f"Answer: {result}"

    except (SyntaxError, ZeroDivisionError, TypeError):
        return "Invalid calculation. Please try again."


def get_study_tips():
    """Tool: Provide useful study suggestions."""

    return (
        "Study Tips:\n"
        "1. Create a daily study timetable.\n"
        "2. Revise topics regularly.\n"
        "3. Practise previous question papers.\n"
        "4. Take short breaks while studying.\n"
        "5. Practise coding and aptitude every day."
    )


def college_assistant():
    """Main agent: Understand the question and select a tool."""

    print("\nI am your College Assistant Agent.")
    print("Ask me about courses, admissions, exams, placements,")
    print("fees, library, scholarships, or study tips.")
    print("Type 'help' to see options or 'exit' to stop.")

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Agent: Please enter a question.")
            continue

        question = user_input.lower()

        # Handle exit
        if question in ["exit", "quit", "bye"]:
            print("Agent: Thank you for using the College Assistant!")
            break

        # Display available features
        elif question == "help":
            print("\nAgent: You can ask about:")
            print("- Courses and departments")
            print("- Admission and fees")
            print("- Library and examinations")
            print("- Placements and attendance")
            print("- Scholarships and timetable")
            print("- Date and time")
            print("- Calculator")
            print("- Study tips")

        # Tool selection: date and time
        elif any(word in question for word in ["date", "time", "today"]):
            print("Agent:", get_date_time())

        # Tool selection: calculator
        elif question.startswith("calculate "):
            expression = user_input[len("calculate "):]
            print("Agent:", calculate(expression))

        # Tool selection: study tips
        elif "study tips" in question or "how to study" in question:
            print("Agent:", get_study_tips())

        # Search the college knowledge base
        else:
            answer = search_knowledge(user_input)

            if answer:
                print("Agent:", answer)
            else:
                print(
                    "Agent: Sorry, I don't have that information yet. "
                    "Please contact your college office or ask another "
                    "college-related question."
                )


# Start the agent
if __name__ == "__main__":
    college_assistant()
