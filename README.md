# AI Chat Assistant

A sleek, modern AI chat application powered by Groq LLM API. This Flask-based application provides an intuitive interface for interacting with state-of-the-art language models.

![AI Chat Assistant Screenshot](https://api.placeholder.com/800/400)

## Features

- 🤖 Integration with Groq's powerful LLM models
- 💬 Clean, responsive chat interface
- ⚡ Real-time interaction with typing indicators
- 🎨 Modern UI with smooth animations
- 🔒 Session management for user conversations
- 📱 Mobile-friendly design

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI API**: Groq LLM API
- **Styling**: Custom CSS with responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/srikanth-thirumani/ai-chat-assistant.git
   cd ai-chat-assistant
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Configuration

You can modify the application settings by changing the following parameters in `app.py`:

- **LLM Model**: Change the model in the chat endpoint (`llama3-70b-8192` is used by default)
- **Temperature**: Adjust the creativity level of responses
- **Max Tokens**: Set the maximum length of responses

## Directory Structure

```
ai-chat-assistant/
├── app.py                # Main Flask application
├── templates/
│   └── index2.html       # Chat interface
├── static/
│   ├── css/              # Additional CSS (if needed)
│   ├── js/               # Additional JS (if needed)
│   └── img/              # Images used in the application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| GROQ_API_KEY | Your Groq API key for accessing LLM models |

## Deployment

### Docker

1. Build the Docker image:
   ```bash
   docker build -t ai-chat-assistant .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 -e GROQ_API_KEY=your_api_key_here ai-chat-assistant
   ```

### Heroku

1. Create a Heroku app:
   ```bash
   heroku create your-app-name
   ```

2. Set the API key:
   ```bash
   heroku config:set GROQ_API_KEY=your_api_key_here
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

## API Endpoints

- `GET /`: Main chat interface
- `POST /chat`: Endpoint for sending messages to the AI
- `GET /get_history`: Returns chat history (currently returns empty array)
- `GET /get_all_data`: Admin endpoint to view all conversations (currently returns empty array)

## Customization

### Changing the Chat Interface

The chat interface is contained in `templates/index2.html`. You can modify the CSS styles directly in this file to customize the appearance.

### Using Different LLM Models

You can change the model by updating the `model` parameter in the payload:

```python
payload = {
    "model": "your-preferred-model",  # Change this to your preferred model
    "messages": messages,
    "temperature": 0.7,
    "max_tokens": 1000
}
```

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Groq](https://console.groq.com/) for their powerful LLM API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Font Awesome](https://fontawesome.com/) for the icons used in the UI

---

Made with ❤️ by [Thirumani Srikanth](https://github.com/srikanth-thirumani)
