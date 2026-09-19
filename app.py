import streamlit as st
import pandas as pd
from datetime import date, timedelta
import math


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Study Planner Pro",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 5% 5%, #E9F8FF 0%, transparent 25%),
        radial-gradient(circle at 95% 5%, #F6E9FF 0%, transparent 25%),
        linear-gradient(135deg, #F8FCFF 0%, #FFF9FC 50%, #F8F5FF 100%);
}

/* Main area */
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #10264A 0%,
        #08172F 100%
    );
}

[data-testid="stSidebar"] * {
    color: #F4F8FF;
}

[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
    background-color: #19345F !important;
    color: white !important;
    border: 1px solid #3A5C8C !important;
}

[data-testid="stSidebar"] input::placeholder,
[data-testid="stSidebar"] textarea::placeholder {
    color: #B9C8DF !important;
}

/* Hero */
.hero-box {
    width: 100%;
    min-height: 155px;
    padding: 30px 35px;
    box-sizing: border-box;

    border-radius: 24px;

    background: linear-gradient(
        110deg,
        #B9EDFF 0%,
        #DCE7FF 38%,
        #F0D9FF 70%,
        #FFE8D8 100%
    );

    box-shadow: 0 8px 30px rgba(55, 90, 140, 0.12);

    margin-bottom: 25px;
}

.hero-title {
    color: #09183F;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 10px;
}

.hero-subtitle {
    color: #193B78;
    font-size: 17px;
    line-height: 1.5;
}

/* Feature cards */
.feature-card {
    min-height: 175px;
    padding: 22px 15px;
    border-radius: 19px;

    text-align: center;

    border: 1px solid rgba(80, 110, 160, 0.16);

    box-shadow: 0 5px 18px rgba(40, 70, 110, 0.07);

    box-sizing: border-box;
}

.feature-icon {
    font-size: 40px;
    margin-bottom: 8px;
}

.feature-title {
    color: #142B61;
    font-size: 18px;
    font-weight: 800;
    line-height: 1.25;
}

.feature-description {
    color: #52698F;
    font-size: 14px;
    line-height: 1.5;
    margin-top: 10px;
}

.blue-card {
    background: linear-gradient(135deg, #EFF9FF, #E7F3FF);
}

.yellow-card {
    background: linear-gradient(135deg, #FFF9E8, #FFF3D7);
}

.purple-card {
    background: linear-gradient(135deg, #F8F0FF, #F1E7FF);
}

.green-card {
    background: linear-gradient(135deg, #ECFFF7, #E4FAF1);
}

.pink-card {
    background: linear-gradient(135deg, #FFF0F5, #FFE8F0);
}

/* Welcome card */
.welcome-card {
    min-height: 235px;
    padding: 27px;
    border-radius: 21px;

    background: rgba(255, 255, 255, 0.96);

    border: 1px solid #DFE9F5;

    box-shadow: 0 6px 22px rgba(50, 80, 120, 0.07);

    box-sizing: border-box;
}

.welcome-title {
    color: #102966;
    font-size: 27px;
    font-weight: 800;
    line-height: 1.3;
}

.welcome-subtitle {
    color: #254A82;
    font-size: 17px;
    font-weight: 600;
    margin-top: 13px;
}

.welcome-text {
    color: #53698E;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 12px;
}

.goal-box {
    display: inline-block;
    margin-top: 15px;
    padding: 11px 17px;

    background: #EEF8FF;

    border: 1px solid #D7EDFF;
    border-radius: 12px;

    color: #1768A5;
    font-weight: 700;
}

/* Quote card */
.quote-card {
    min-height: 235px;
    padding: 27px;

    border-radius: 21px;

    background: linear-gradient(
        135deg,
        #F4EEFF,
        #FFF0F8
    );

    border: 1px solid #E7DDF7;

    box-shadow: 0 6px 22px rgba(100, 70, 130, 0.07);

    text-align: center;
    box-sizing: border-box;
}

.quote-text {
    color: #54249B;
    font-size: 25px;
    font-weight: 800;
    font-style: italic;
    line-height: 1.45;
}

.quote-small {
    color: #5D6C89;
    font-size: 16px;
    font-weight: 600;
    margin-top: 16px;
}

.quote-icon {
    font-size: 52px;
    margin-top: 15px;
}

/* Section title */
.section-title {
    color: #102966;
    font-size: 27px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Process cards */
.process-card {
    min-height: 165px;
    padding: 17px 10px;

    background: rgba(255,255,255,0.90);

    border: 1px solid #DFE8F5;
    border-radius: 18px;

    text-align: center;

    box-shadow: 0 4px 15px rgba(50,80,120,0.06);
}

.process-icon {
    font-size: 34px;
}

.process-title {
    color: #17326D;
    font-weight: 800;
    font-size: 15px;
    margin-top: 7px;
}

.process-text {
    color: #5B6E8E;
    font-size: 12px;
    line-height: 1.45;
    margin-top: 8px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64738F;
    font-size: 14px;
    padding: 30px 10px;
}

/* Buttons */
.stButton > button {
    border-radius: 12px !important;
    font-weight: 700 !important;
    min-height: 44px !important;
}

/* Dataframe */
.stDataFrame {
    border-radius: 14px;
    overflow: hidden;
}

/* Metrics */
[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #E1E9F5;
    box-shadow: 0 3px 12px rgba(40,70,110,0.05);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "plan" not in st.session_state:
    st.session_state.plan = None

if "generation_count" not in st.session_state:
    st.session_state.generation_count = 0


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def parse_items(text):
    """Convert comma/newline separated text into a list."""

    if not text:
        return []

    text = text.replace("\n", ",")

    items = [item.strip() for item in text.split(",")]

    return [item for item in items if item]


def create_tasks(subject):
    """Break one subject into smaller tasks."""

    return [
        f"{subject} - Concept Review",
        f"{subject} - Important Topics",
        f"{subject} - Practice Questions",
        f"{subject} - Revision"
    ]


def get_priority(subject, priority_topics, weak_subjects):
    """Calculate priority score."""

    score = 1

    subject_lower = subject.lower()

    for item in priority_topics:

        item_lower = item.lower()

        if (
            item_lower in subject_lower
            or subject_lower in item_lower
        ):
            score += 2

    for item in weak_subjects:

        item_lower = item.lower()

        if (
            item_lower in subject_lower
            or subject_lower in item_lower
        ):
            score += 2

    return score


def build_schedule(
    start_date,
    exam_date,
    hours_per_day,
    subjects,
    priority_topics,
    weak_subjects,
    study_days,
    strategy,
    add_revision,
    add_mock
):
    """Generate the complete study schedule."""

    if exam_date <= start_date:
        return pd.DataFrame(), "Exam date must be after the start date."

    if not subjects:
        return pd.DataFrame(), "Please enter at least one subject."

    if not study_days:
        return pd.DataFrame(), "Please select at least one study day."

    selected_dates = []

    current_date = start_date

    while current_date < exam_date:

        day_name = current_date.strftime("%a")

        if day_name in study_days:
            selected_dates.append(current_date)

        current_date += timedelta(days=1)

    if not selected_dates:
        return (
            pd.DataFrame(),
            "No selected study days are available between the dates."
        )

    selected_dates = selected_dates[:60]

    weights = {}

    for subject in subjects:

        weights[subject] = get_priority(
            subject,
            priority_topics,
            weak_subjects
        )

    total_weight = sum(weights.values())

    rows = []

    task_pointer = {
        subject: 0
        for subject in subjects
    }

    for day_index, study_date in enumerate(selected_dates):

        total_daily_minutes = int(hours_per_day * 60)

        extra_minutes = 0

        if add_revision:
            extra_minutes += min(
                30,
                max(20, total_daily_minutes // 8)
            )

        if add_mock and (day_index + 1) % 7 == 0:
            extra_minutes += min(
                45,
                max(30, total_daily_minutes // 6)
            )

        study_minutes = max(
            30,
            total_daily_minutes - extra_minutes
        )

        # ----------------------------------------------
        # Strategy
        # ----------------------------------------------

        if strategy == "Priority First":

            ordered_subjects = sorted(
                subjects,
                key=lambda x: weights[x],
                reverse=True
            )

        elif strategy == "Easy First":

            ordered_subjects = sorted(
                subjects,
                key=lambda x: weights[x]
            )

        else:

            ordered_subjects = subjects[:]

            if ordered_subjects:

                shift = day_index % len(ordered_subjects)

                ordered_subjects = (
                    ordered_subjects[shift:]
                    + ordered_subjects[:shift]
                )

        number_of_subjects = min(
            len(ordered_subjects),
            max(1, math.ceil(study_minutes / 90))
        )

        selected_subjects = ordered_subjects[
            :number_of_subjects
        ]

        if strategy == "Priority First":

            allocations = {}

            for subject in selected_subjects:

                allocations[subject] = max(
                    30,
                    int(
                        study_minutes
                        * weights[subject]
                        / total_weight
                    )
                )

            allocation_total = sum(
                allocations.values()
            )

            if allocation_total > study_minutes:

                factor = (
                    study_minutes
                    / allocation_total
                )

                for subject in allocations:

                    allocations[subject] = max(
                        30,
                        int(
                            allocations[subject]
                            * factor
                        )
                    )

        else:

            base = study_minutes // len(
                selected_subjects
            )

            allocations = {
                subject: base
                for subject in selected_subjects
            }

        # ----------------------------------------------
        # Create study tasks
        # ----------------------------------------------

        remaining = study_minutes

        for index, subject in enumerate(selected_subjects):

            duration = allocations[subject]

            if index == len(selected_subjects) - 1:
                duration = max(
                    30,
                    remaining
                )

            duration = min(
                duration,
                remaining
            )

            if duration <= 0:
                continue

            tasks = create_tasks(subject)

            task = tasks[
                task_pointer[subject]
                % len(tasks)
            ]

            task_pointer[subject] += 1

            priority = (
                "High"
                if weights[subject] >= 3
                else "Normal"
            )

            rows.append({
                "Date": study_date,
                "Day": study_date.strftime("%A"),
                "Subject": subject,
                "Task": task,
                "Duration (min)": duration,
                "Priority": priority,
                "Type": "Study"
            })

            remaining -= duration

            if remaining <= 0:
                break

        # ----------------------------------------------
        # Revision
        # ----------------------------------------------

        if add_revision:

            revision_minutes = min(
                30,
                max(20, total_daily_minutes // 8)
            )

            rows.append({
                "Date": study_date,
                "Day": study_date.strftime("%A"),
                "Subject": "Revision",
                "Task": "Review previous topics",
                "Duration (min)": revision_minutes,
                "Priority": "High",
                "Type": "Revision"
            })

        # ----------------------------------------------
        # Mini mock test
        # ----------------------------------------------

        if add_mock and (day_index + 1) % 7 == 0:

            mock_minutes = min(
                45,
                max(30, total_daily_minutes // 6)
            )

            rows.append({
                "Date": study_date,
                "Day": study_date.strftime("%A"),
                "Subject": "All Subjects",
                "Task": "Mini Mock Test",
                "Duration (min)": mock_minutes,
                "Priority": "High",
                "Type": "Mock Test"
            })

    result = pd.DataFrame(rows)

    return result, "Study plan generated successfully."


def evaluate_plan(
    dataframe,
    hours_per_day,
    exam_date
):
    """Evaluate time and priority constraints."""

    if dataframe.empty:

        return {
            "score": 0,
            "status": "Not Ready",
            "message": "No study plan is available."
        }

    daily_limit = int(
        hours_per_day * 60
    )

    daily_total = (
        dataframe
        .groupby("Date")["Duration (min)"]
        .sum()
    )

    time_constraint = bool(
        (daily_total <= daily_limit).all()
    )

    priority_constraint = bool(
        (dataframe["Priority"] == "High").any()
    )

    last_date = dataframe["Date"].max()

    if isinstance(last_date, pd.Timestamp):
        last_date = last_date.date()

    exam_constraint = last_date < exam_date

    checks = sum([
        time_constraint,
        priority_constraint,
        exam_constraint
    ])

    score = int(
        (checks / 3) * 100
    )

    if score == 100:

        status = "Excellent"

        message = (
            "All main time and priority constraints "
            "are satisfied."
        )

    elif score >= 66:

        status = "Good"

        message = (
            "Most planning constraints are satisfied."
        )

    else:

        status = "Needs Refinement"

        message = (
            "Some planning constraints need refinement."
        )

    return {
        "score": score,
        "status": status,
        "message": message
    }


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:8px 5px 15px 5px;
        ">
            <div style="font-size:52px;">📚</div>

            <div style="
                font-size:25px;
                font-weight:800;
                color:white;
            ">
                AI Study Planner Pro
            </div>

            <div style="
                color:#73D7FF;
                font-size:15px;
                margin-top:6px;
            ">
                Plan • Learn • Achieve
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 📌 Study Constraints")

    start_date = st.date_input(
        "Start Date",
        value=date.today()
    )

    exam_date = st.date_input(
        "Exam Date",
        value=date.today() + timedelta(days=14)
    )

    available_hours = st.number_input(
        "Available Study Hours Per Day",
        min_value=1.0,
        max_value=12.0,
        value=4.0,
        step=0.5
    )

    st.markdown("### 📚 Subjects")

    subjects_text = st.text_area(
        "Subjects",
        value="Python, Database, AI, Blockchain",
        height=80
    )

    st.markdown("### ⭐ Priority Topics")

    priority_text = st.text_area(
        "Priority Topics",
        value="AI, Python",
        height=80
    )

    st.markdown("### 🧠 Advanced Features")

    weak_text = st.text_input(
        "Difficult / Weak Subjects",
        value="Database"
    )

    strategy = st.selectbox(
        "Planning Strategy",
        [
            "Priority First",
            "Balanced",
            "Easy First"
        ]
    )

    st.markdown("### 📅 Study Days")

    day_col1, day_col2 = st.columns(2)

    selected_days = []

    with day_col1:

        if st.checkbox(
            "Mon",
            value=True
        ):
            selected_days.append("Mon")

        if st.checkbox(
            "Wed",
            value=True
        ):
            selected_days.append("Wed")

        if st.checkbox(
            "Fri",
            value=True
        ):
            selected_days.append("Fri")

        if st.checkbox(
            "Sun",
            value=False
        ):
            selected_days.append("Sun")

    with day_col2:

        if st.checkbox(
            "Tue",
            value=True
        ):
            selected_days.append("Tue")

        if st.checkbox(
            "Thu",
            value=True
        ):
            selected_days.append("Thu")

        if st.checkbox(
            "Sat",
            value=False
        ):
            selected_days.append("Sat")

    add_revision = st.checkbox(
        "🔄 Add Revision Sessions",
        value=True
    )

    add_mock = st.checkbox(
        "📝 Add Mini Mock Tests",
        value=True
    )

    st.markdown("")

    generate_clicked = st.button(
        "🚀 Generate Study Plan",
        use_container_width=True
    )


# ============================================================
# HERO HEADER
# ============================================================

st.html(
    """
    <div class="hero-box">

        <div class="hero-title">
            📚 AI Study Planner Pro
        </div>

        <div class="hero-subtitle">
            Smart Study Planning • Priority Management •
            Task Decomposition • Analytics • Progress Tracking
        </div>

    </div>
    """
)


# ============================================================
# FEATURE CARDS
# ============================================================

feature_data = [
    (
        "🧩",
        "Task Decomposition",
        "Break subjects into smaller detailed tasks",
        "blue-card"
    ),
    (
        "⭐",
        "Priority Handling",
        "Give more time to important topics",
        "yellow-card"
    ),
    (
        "🧠",
        "Difficulty Analysis",
        "Identify weak and hard subjects",
        "purple-card"
    ),
    (
        "📅",
        "Schedule Generation",
        "Create a personalized study timetable",
        "green-card"
    ),
    (
        "🔄",
        "Iterative Refinement",
        "Regenerate the plan when needed",
        "pink-card"
    )
]

feature_columns = st.columns(5)

for column, feature in zip(
    feature_columns,
    feature_data
):

    icon, title, description, css_class = feature

    with column:

        st.html(
            f"""
            <div class="feature-card {css_class}">

                <div class="feature-icon">
                    {icon}
                </div>

                <div class="feature-title">
                    {title}
                </div>

                <div class="feature-description">
                    {description}
                </div>

            </div>
            """
        )


# ============================================================
# WELCOME + QUOTE
# ============================================================

welcome_column, quote_column = st.columns(
    [2, 1],
    gap="large"
)

with welcome_column:

    st.html(
        """
        <div class="welcome-card">

            <div class="welcome-title">
                🎯 Welcome to AI Study Planner Pro!
            </div>

            <div class="welcome-subtitle">
                Your personalized study plan is just a click away.
            </div>

            <div class="welcome-text">
                Fill in the details from the sidebar and click
                <b>Generate Study Plan</b> to get your smart schedule.
            </div>

            <div class="goal-box">
                💡 Your goals + Smart planning = Success
            </div>

        </div>
        """
    )


with quote_column:

    st.html(
        """
        <div class="quote-card">

            <div class="quote-text">
                “Small steps every day
                lead to big results.”
            </div>

            <div class="quote-small">
                Keep going! 💪
            </div>

            <div class="quote-icon">
                🏔️
            </div>

        </div>
        """
    )


# ============================================================
# HOW IT WORKS
# ============================================================

st.html(
    """
    <div class="section-title">
        ✨ How It Works?
    </div>
    """
)

process_data = [
    (
        "📄",
        "1. Input Constraints",
        "Subjects, hours, exam date and priority topics"
    ),
    (
        "🧩",
        "2. Task Decomposition",
        "Divide subjects into smaller tasks"
    ),
    (
        "👥",
        "3. Priority Handling",
        "Give extra time to priority topics"
    ),
    (
        "📅",
        "4. Schedule Generation",
        "Create timetable within time limits"
    ),
    (
        "✅",
        "5. Evaluation",
        "Check time and priority constraints"
    ),
    (
        "🔄",
        "6. Regeneration",
        "Update inputs and create a new plan"
    )
]

process_columns = st.columns(6)

for column, process in zip(
    process_columns,
    process_data
):

    icon, title, description = process

    with column:

        st.html(
            f"""
            <div class="process-card">

                <div class="process-icon">
                    {icon}
                </div>

                <div class="process-title">
                    {title}
                </div>

                <div class="process-text">
                    {description}
                </div>

            </div>
            """
        )


# ============================================================
# GENERATE PLAN
# ============================================================

if generate:

    subjects = parse_items(
        subjects_text
    )

    priority_topics = parse_items(
        priority_text
    )

    weak_subjects = parse_items(
        weak_text
    )

    with st.spinner(
        "🧠 Building your personalized study plan..."
    ):

        generated_plan, message = build_schedule(
            start_date=start_date,
            exam_date=exam_date,
            hours_per_day=available_hours,
            subjects=subjects,
            priority_topics=priority_topics,
            weak_subjects=weak_subjects,
            study_days=selected_days,
            strategy=strategy,
            add_revision=add_revision,
            add_mock=add_mock
        )

    if generated_plan.empty:

        st.error(message)

    else:

        st.session_state.plan = generated_plan

        st.session_state.generation_count += 1

        st.success(
            f"✅ {message} "
            f"Generation #{st.session_state.generation_count}"
        )


# ============================================================
# GENERATED PLAN DASHBOARD
# ============================================================

if st.session_state.plan is not None:

    dataframe = st.session_state.plan.copy()

    st.html(
        """
        <div class="section-title">
            📊 Your Personalized Study Dashboard
        </div>
        """
    )

    total_minutes = int(
        dataframe["Duration (min)"].sum()
    )

    total_hours = round(
        total_minutes / 60,
        1
    )

    study_tasks = int(
        (
            dataframe["Type"] == "Study"
        ).sum()
    )

    high_priority = int(
        (
            dataframe["Priority"] == "High"
        ).sum()
    )

    number_of_days = int(
        dataframe["Date"].nunique()
    )

    metric1, metric2, metric3, metric4, metric5 = st.columns(5)

    metric1.metric(
        "📅 Study Days",
        number_of_days
    )

    metric2.metric(
        "⏱️ Total Hours",
        total_hours
    )

    metric3.metric(
        "📝 Tasks",
        study_tasks
    )

    metric4.metric(
        "⭐ High Priority",
        high_priority
    )

    metric5.metric(
        "🔄 Generation",
        st.session_state.generation_count
    )


    # ========================================================
    # PLAN EVALUATION
    # ========================================================

    st.html(
        """
        <div class="section-title">
            🔍 Plan Evaluation
        </div>
        """
    )

    evaluation = evaluate_plan(
        dataframe,
        available_hours,
        exam_date
    )

    evaluation1, evaluation2, evaluation3 = st.columns(3)

    with evaluation1:

        st.metric(
            "Evaluation Score",
            f"{evaluation['score']}%"
        )

    with evaluation2:

        st.metric(
            "Status",
            evaluation["status"]
        )

    with evaluation3:

        st.info(
            evaluation["message"]
        )


    # ========================================================
    # STRUCTURED PROMPT
    # ========================================================

    st.html(
        """
        <div class="section-title">
            🧠 Structured Prompt Used
        </div>
        """
    )

    structured_prompt = f"""
ROLE:
You are an intelligent study planning assistant.

GOAL:
Create a personalized study schedule.

INPUT CONSTRAINTS:
Start Date: {start_date}
Exam Date: {exam_date}
Available Hours Per Day: {available_hours}
Subjects: {subjects_text}
Priority Topics: {priority_text}
Difficult Subjects: {weak_text}
Planning Strategy: {strategy}
Study Days: {", ".join(selected_days)}

TASK DECOMPOSITION:
Break each subject into smaller study tasks.

PRIORITY HANDLING:
Give additional attention to priority and weak subjects.

SCHEDULE GENERATION:
Create a study timetable within the available daily time.

EVALUATION:
Check time limits and priority constraints.

ITERATIVE REFINEMENT:
If inputs are changed, generate a new study plan.
"""

    st.code(
        structured_prompt.strip(),
        language="text"
    )


    # ========================================================
    # TABS
    # ========================================================

    tab_schedule, tab_tasks, tab_analytics, tab_refinement = st.tabs(
        [
            "📅 Study Schedule",
            "🧩 Task Decomposition",
            "📈 Analytics",
            "🔄 Refinement"
        ]
    )


    # ========================================================
    # STUDY SCHEDULE
    # ========================================================

    with tab_schedule:

        st.subheader(
            "📅 Generated Study Plan"
        )

        display_dataframe = dataframe.copy()

        display_dataframe["Date"] = (
            display_dataframe["Date"]
            .astype(str)
        )

        st.dataframe(
            display_dataframe,
            use_container_width=True,
            hide_index=True
        )

        csv_file = display_dataframe.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "📥 Download Study Plan",
            data=csv_file,
            file_name="AI_Study_Plan.csv",
            mime="text/csv",
            use_container_width=True
        )


    # ========================================================
    # TASK DECOMPOSITION
    # ========================================================

    with tab_tasks:

        st.subheader(
            "🧩 Task Decomposition"
        )

        unique_subjects = (
            dataframe["Subject"]
            .unique()
        )

        for subject in unique_subjects:

            if subject in [
                "Revision",
                "All Subjects"
            ]:
                continue

            st.markdown(
                f"### 📘 {subject}"
            )

            tasks = create_tasks(
                subject
            )

            for number, task in enumerate(
                tasks,
                start=1
            ):

                st.write(
                    f"**{number}.** {task}"
                )


    # ========================================================
    # ANALYTICS
    # ========================================================

    with tab_analytics:

        st.subheader(
            "📈 Study Analytics"
        )

        subject_minutes = (
            dataframe
            .groupby("Subject")[
                "Duration (min)"
            ]
            .sum()
            .sort_values(
                ascending=False
            )
        )

        chart_dataframe = (
            subject_minutes
            .to_frame("Minutes")
        )

        st.bar_chart(
            chart_dataframe
        )

        st.markdown(
            "#### 📊 Subject-wise Study Time"
        )

        st.dataframe(
            chart_dataframe,
            use_container_width=True
        )


    # ========================================================
    # ITERATIVE REFINEMENT
    # ========================================================

    with tab_refinement:

        st.subheader(
            "🔄 Iterative Refinement"
        )

        st.write(
            """
            Change any study constraint in the sidebar
            and generate the plan again.

            The application follows:

            Input → Generate → Evaluate → Modify → Regenerate
            """
        )

        st.info(
            "💡 This demonstrates iterative refinement "
            "in the Prompt Engineering workflow."
        )

        regenerate_button = st.button(
            "♻️ Regenerate Current Plan",
            use_container_width=True
        )

        if regenerate_button:

            subjects = parse_items(
                subjects_text
            )

            priority_topics = parse_items(
                priority_text
            )

            weak_subjects = parse_items(
                weak_text
            )

            new_plan, new_message = build_schedule(
                start_date,
                exam_date,
                available_hours,
                subjects,
                priority_topics,
                weak_subjects,
                selected_days,
                strategy,
                add_revision,
                add_mock
            )

            if new_plan.empty:

                st.error(
                    new_message
                )

            else:

                st.session_state.plan = new_plan

                st.session_state.generation_count += 1

                st.success(
                    "♻️ New study plan generated successfully!"
                )

                st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">

        📚 <b>AI Study Planner Pro</b>

        <br><br>

        Smart Planning • Priority Management •
        Task Decomposition • Analytics • Iterative Refinement

        <br><br>

        🌱 Stay Focused • Be Consistent • Achieve Your Goals

    </div>
    """
)