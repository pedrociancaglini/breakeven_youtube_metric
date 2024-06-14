```markdown
# YouTube Breakeven Point Calculator

This Streamlit app calculates the breakeven point for a YouTube channel based on the current subscribers, watch hours, daily growth rates, and historical data. It provides a forecast of when the channel will reach 1000 subscribers and 4000 watch hours, displaying the results in a graph.

## Features

- Input current subscribers and watch hours.
- Input daily new subscribers and watch hours.
- Input historical subscriber and watch hour data.
- Automatically calculate growth rates based on historical data.
- Calculate the number of days to reach 1000 subscribers and 4000 watch hours.
- Display a forecast graph of subscriber and watch hour growth.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/youtube-breakeven-calculator.git
cd youtube-breakeven-calculator
```

2. Install the required packages:

```sh
pip install streamlit pandas matplotlib
```

## Usage

1. Run the Streamlit app:

```sh
streamlit run youtube_breakeven.py
```

2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to input your current statistics, daily growth rates, and historical data.

4. View the results and forecast graph.

## File Structure

```
.
├── youtube_breakeven.py
├── README.md
└── requirements.txt
```

- `youtube_breakeven.py`: The main Streamlit application file.
- `README.md`: This readme file.
- `requirements.txt`: List of dependencies for the project.

## Dependencies

- `streamlit`
- `pandas`
- `matplotlib`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Replace `https://github.com/yourusername/youtube-breakeven-calculator.git` with the actual URL of your GitHub repository. The `requirements.txt` file should contain the dependencies:

```
streamlit
pandas
matplotlib
```
