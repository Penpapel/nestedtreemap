import streamlit as st
import matplotlib.pyplot as plt
import squarify  # For creating treemaps
import random

# Function to create and display a treemap
def display_treemap(level, data_key=None):
    fig, ax = plt.subplots()

    if level == 1:
        data = treemap_data[1]
        st.session_state.current_data_key = None
    elif level == 2:
        data = treemap_data[1]['next_level'][data_key]
        st.session_state.current_data_key = data_key
    elif level == 3:
        data = treemap_data[2]['next_level'][data_key]

    labels = data['labels']
    values = data['values']

    # Normalize sizes and create the treemap layout
    values_norm = squarify.normalize_sizes(values, 1, 1)  # Normalized for a square (1x1)
    rects = squarify.squarify(values_norm, 0, 0, 1, 1)

    # Plot each rectangle manually
    for i, rect in enumerate(rects):
        label = labels[i]
        color = plt.cm.Blues(random.random())  # Random color
        ax.add_patch(plt.Rectangle((rect['x'], rect['y']), rect['dx'], rect['dy'], color=color, alpha=0.7))
        ax.text(rect['x'] + rect['dx']/2, rect['y'] + rect['dy']/2, label, va="center", ha="center", fontsize=10)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    st.pyplot(fig)

# Initialize session state
if 'current_level' not in st.session_state:
    st.session_state.current_level = 1
    st.session_state.current_data_key = None
    st.session_state.previous_states = []

# Sample Data
treemap_data = {
    1: {
        'labels': ['Project A', 'Project B', 'Project C'],
        'values': [random.randint(10, 100) for _ in range(3)],
        'next_level': {
            'Project A': {
                'labels': [f'Task A{i+1}' for i in range(9)],
                'values': [random.randint(5, 50) for _ in range(9)]
            },
            'Project B': {
                'labels': [f'Task B{i+1}' for i in range(9)],
                'values': [random.randint(5, 50) for _ in range(9)]
            },
            'Project C': {
                'labels': [f'Task C{i+1}' for i in range(9)],
                'values': [random.randint(5, 50) for _ in range(9)]
            }
        }
    },
    2: {
        'next_level': {
            'Task A1': {'labels': [f'Subtask A1-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A2': {'labels': [f'Subtask A2-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A3': {'labels': [f'Subtask A3-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A4': {'labels': [f'Subtask A4-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A5': {'labels': [f'Subtask A5-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A6': {'labels': [f'Subtask A6-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A7': {'labels': [f'Subtask A7-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A8': {'labels': [f'Subtask A8-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task A9': {'labels': [f'Subtask A9-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},

            'Task B1': {'labels': [f'Subtask B1-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B2': {'labels': [f'Subtask B2-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B3': {'labels': [f'Subtask B3-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B4': {'labels': [f'Subtask B4-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B5': {'labels': [f'Subtask B5-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B6': {'labels': [f'Subtask B6-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B7': {'labels': [f'Subtask B7-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B8': {'labels': [f'Subtask B8-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task B9': {'labels': [f'Subtask B9-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},

            'Task C1': {'labels': [f'Subtask C1-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C2': {'labels': [f'Subtask C2-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C3': {'labels': [f'Subtask C3-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C4': {'labels': [f'Subtask C4-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C5': {'labels': [f'Subtask C5-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C6': {'labels': [f'Subtask C6-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C7': {'labels': [f'Subtask C7-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C8': {'labels': [f'Subtask C8-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]},
            'Task C9': {'labels': [f'Subtask C9-{i+1}' for i in range(27)], 'values': [random.randint(1, 10) for _ in range(27)]}
        }
    }
}

# Treemap Rendering and Navigation
st.title("Nested Treemap with Streamlit")

# Display current treemap
display_treemap(st.session_state
