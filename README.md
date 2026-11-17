# 📰 News Fetcher – AI-Powered News Retrieval

A Python-based news retrieval application that uses the **Akta News API** to fetch news articles based on user-selected genres and topics. Users can interact with the application through a command-line interface (CLI), select a news category, enter a topic of interest, and retrieve relevant news articles.

## 🚀 Features

- **Genre-Based News Selection:** Choose from five different news categories:
  - Sports
  - Politics
  - Science
  - Business
  - Technology
- **Topic-Based Search:** Search for specific topics within a selected news category.
- **API Integration:** Fetch news articles using the Akta News API.
- **Environment Variable Support:** Securely manage API credentials using a `.env` file.
- **Interactive CLI:** Simple menu-driven interface for a smooth user experience.

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – For making HTTP requests to the News API.
- **Python-Dotenv** – For loading environment variables.
- **Akta News API** – For retrieving news articles.

## 📂 Project Structure

```text
News-Fetcher/
│
├── main.py              # Main application
├── .env                 # API credentials (not committed)
├── .gitignore           # Files excluded from Git
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/News-Fetcher.git
```

### 2. Navigate to the Project Directory

```bash
cd News-Fetcher
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Credentials

Create a `.env` file in the root directory and add your Akta News API key:

```env
NEWS_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

### 6. Run the Application

```bash
python main.py
```

## 💻 Usage

Once the application starts, you will see the following menu:

```text
What Genre of news Do you want?

1. Sports
2. Politics
3. Science
4. Business
5. Tech
0. Exit
```

**Example:**

```text
What Genre of news Do you want?
1. Sports
2. Politics
3. Science
4. Business
5. Tech
0. Exit

Enter your choice: 5

What would you like to know about Tech?
> Artificial Intelligence

[News Article Content]
```

The application retrieves a relevant news article based on the selected genre and topic.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `NEWS_API_KEY` | API key required to authenticate requests to Akta News API |

**Important:** Never upload your `.env` file or expose your API key publicly.

Add the following to your `.gitignore` file:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
requests
python-dotenv
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🔮 Future Improvements

- [ ] Display multiple news articles instead of a single result.
- [ ] Add exception handling for network errors and API failures.
- [ ] Implement input validation for user selections.
- [ ] Add support for more news categories.
- [ ] Introduce a graphical user interface (GUI).
- [ ] Implement AI-powered news summarization.
- [ ] Add multilingual news retrieval support.

## 👨‍💻 Author

**Varun Yadgude**

- GitHub: [Your GitHub Profile](https://github.com/YOUR_USERNAME)

---

⭐ If you find this project interesting, consider giving it a star!