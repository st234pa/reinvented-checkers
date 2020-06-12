# Reinvented Checkers Django Client App

## Setup (for Mac)

### Node

- Make sure you have [node and npm](https://nodejs.org/en/download/) installed. If you don't have it installed, use the macOS installer.
- Make sure you have [yarn](https://classic.yarnpkg.com/en/docs/install#mac-stable) installed.
- Clone this repository. From the `reinvented-checkers/client/app` directories install dependancies.
```
:app $ yarn
```

### Expo

- Install the Expo CLI command line utility.
```
npm install -g expo-cli
```
- On your phone, install the Expo Client app from App Store or Google Play.

## Running the app locally

- Run the API locally following the instructions from `api/README.md`.
- In the `reinvented-checkers/client/app` directory, run a local Metro server for the app.
```
:app $ yarn start
```
- Make sure your phone is connected to the same network as the Metro server.
- Run the app on your phone in Expo Client. For an iPhone, use the Camera app to scan the QR code, which shoud result in a notification that opens the app in Expo when you open it.
