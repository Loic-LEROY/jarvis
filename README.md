
<div align="center">
    <img src="jarvis.svg" alt="Jarvis Logo">
</div>

# Jarvis - Local AI Assistant

Jarvis is a local AI assistant that utilizes speech recognition, natural language processing, and text-to-speech synthesis to interact with users.

### Features

- Voice recognition: Jarvis can understand spoken commands and convert them into text.
- Natural language processing: Jarvis uses advanced algorithms to understand the meaning and context of user queries.
- Text-to-speech synthesis: Jarvis can generate human-like speech to respond to user queries.

### Installation
#### Requirements
Before installing J.A.R.V.I.S, you need Python 3.11. You can download it from the official website [here](https://www.python.org/downloads/).

To use Jarvis, follow these steps:

1. Install Linux subsystem for Windows (WSL) if you are using Windows. You can install it by running the following command in PowerShell (or cmd) as an administrator:

    ```bash
    $ wsl --install
    ```
    Follow the on-screen instructions to complete the installation.
2. Install the utility Ollama which is used to launch the IA Mixtral on your computer. To install it, run the following commmands in your terminal:

    ```bash
    $ wsl
    $ curl -fsSL https://ollama.com/install.sh | sh
    ```
3. Install the IA Mixtral by running the following command in your terminal:

    ```bash
    $ ollama run mistral
    ```
    Once the process is complete, you may see a message like this:

    ```bash
    >>> Send a message (/? for help)
    ```
    At this point, you can already interact with the IA Mixtral as if it were a chatbot like ChatGPT. Before launching J.A.R.V.I.S, you must launch Mixtral with the same command as the installation : `ollama run mistral` and keep it open (Do not close your terminal). To exit the chatbot, type `Ctrl + d` or type `/bye` to exit. Then you can close the terminal.
4. Install the required dependencies by running the following command in your termial opened in your J.A.R.V.I.S folder:

    ```bash
    $ pip install -r requirements.txt
    ```
5. Start J.A.R.V.I.S by running the following command:

    ```bash
    $ python jarvis.py
    ```
    Once J.A.R.V.I.S is ready, you will see a message like this:

    ```bash
    --------------------------------------------------------------------------------
    Press Ctrl+C to stop the recording
    --------------------------------------------------------------------------------
    ```
    After this message appears, J.A.R.V.I.S is ready to receive your commands. You can now interact with it by speaking your commands.
    > Tips: : For better results, speak clearly without background noise and wihtout pausing.
6. Speak your command and Jarvis will process it and provide a response.

### Examples

Here are some examples of commands you can use with Jarvis:

- "Jarvis, what is the Pythagoras theorem ?"
- "Jarvis, what is 2.7 x 3.64 ?"
- "Jarvis, how to code in javascript the factorial function ?"

Feel free to explore Jarvis to suit your needs!
