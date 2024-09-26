from modules import manager


if __name__ == "__main__":
    print("Application Starting ... ")
    app = manager.Manager()
    app.mainloop()
    print("Application Closing ...")