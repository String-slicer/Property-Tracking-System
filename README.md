
# Property Tracking System

This is a blockchain-based **Property Tracking System** that uses the **Ethereum blockchain** to provide a secure and efficient way to track properties and transfer ownership. The project is developed using **Truffle**, **Ganache**, **Flask**, and **Python**, ensuring robust backend support and seamless functionality.

## Features

- **Property Tracking**: Track properties securely on the blockchain.
- **Ownership Transfer**: Transfer property ownership easily and transparently.
- **Decentralized Architecture**: Utilizes Ethereum blockchain for a secure and tamper-proof system.
- **User-friendly Interface**: Designed for simplicity and ease of use.

---

## Technologies Used

- **Ethereum Blockchain**: For decentralized property management.
- **Truffle**: Development environment for Ethereum-based smart contracts.
- **Ganache**: Local blockchain for development and testing.
- **Flask**: Python-based backend framework.
- **Python**: Backend programming language.
- **Visual Studio Code**: IDE for coding and debugging.

---

## Project Structure

```
.
├── contracts/          # Solidity smart contracts for the blockchain
├── migrations/         # Deployment scripts for smart contracts
├── node_modules/       # Dependencies for Truffle
├── build/              # Compiled contracts and deployment artifacts
├── backend/
│   ├── app.py          # Flask application
│   ├── routes.py       # API routes for backend functionality
│   ├── static/         # Static files for the application
│   ├── templates/      # HTML templates for the frontend
├── truffle-config.js   # Truffle configuration file
├── package.json        # Node.js dependencies
├── README.md           # Project documentation
```

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Node.js**: [Download Node.js](https://nodejs.org/)
- **Truffle**: Install using `npm install -g truffle`
- **Ganache**: [Download Ganache](https://trufflesuite.com/ganache/)
- **Python**: [Download Python](https://www.python.org/downloads/)
- **Flask**: Install using `pip install flask`

---

## Getting Started

Follow these steps to set up and run the project locally:

### Setting Up the Blockchain

1. Install Truffle and Ganache:
   ```bash
   npm install -g truffle
   ```

2. Open Ganache and create a new workspace.

3. Compile and deploy the smart contracts using Truffle:
   ```bash
   truffle compile
   truffle migrate
   ```

### Setting Up the Backend

1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```bash
   python app.py
   ```

The Flask server will start running at `http://127.0.0.1:5000/`.

---

## Usage

1. Open the web application in your browser.
2. Use the interface to track properties and transfer ownership.
3. Interact with the Ethereum blockchain securely via the app.

---

## Dependencies

Key tools and libraries used:

- **Truffle**: For Ethereum smart contract development.
- **Ganache**: Local Ethereum blockchain.
- **Flask**: Backend framework.
- **Python**: Backend logic.
- **Web3.js**: JavaScript library for interacting with the blockchain.

---

## License

This project is licensed under the MIT License. You are free to use or modify it for personal or educational purposes.

---

## Contact

For any queries or suggestions, feel free to reach out:

- **Email**: harishgupta6301@gmail.com  
- **Location**: Guntur, Andhra Pradesh
