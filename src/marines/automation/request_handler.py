import requests




class RequestHandler():
    def __init__(self):
        self.host = "https://todo.ly/api/"
        self.header = {"Authorization": "Basic Z2F0aXRhMDEwMS5teG1AZ21haWwuY29tOjEyMzQ1Njc4",
          "Content-Type": "application/json"}

