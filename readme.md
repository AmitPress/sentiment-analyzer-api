## Sentiment Analysis API
This is an inference engine that exposes an API endpoint which can be used to classify/analyze different sentiments from raw texts.

#### How to start
First of all, make sure all the dependencies are installed. To do that,
make a `virtual environment` by executing the following command `python -m venv venv`
Now to switch into the environment,
if you're using windows then execute the command `.\venv\Scripts\activate`
or if you're on linux, then try `source venv/bin/activate`.

After doing this, run `pip install -r requirements.txt`. With this command all the required dependencies will be installed. Be patient, it will take some time though.

**Using the app**
To use the application in the local machine run `python app.py`.
Then you can click on the link shown in the terminal to access the application with the url in the browser. You can now check the app with applications like `curl` or you can go with modern gui applications like `postman`.

You can play with the app using the `/docs` endpoint. There you can test the app on the fly.

Now again, to have a wholistic view of the project you can run `pytest tests` on the root directory of the project and again if you want to check the backend application and the API endpoint just run `pytest tests/test_routes.py` and to check the model inference in itself run `pytest tests/test_model.py`.
![Demonstration](/screenshots/demo.png)
#### Technology Stack
This whole app is built with the following packages:
- [SetFit](https://github.com/huggingface/setfit)
- [FastAPI](https://fastapi.tiangolo.com/)

`SetFit` is used for the AI backend.
`FastAPI` is used to expose the inference capability for user consumption.

#### Dataset Description
To fine tune the AI model for our usage, it was needed to train the base model with a custom dataset. And for that purpose I used [this dataset](https://www.kaggle.com/datasets/pradeeshprabhakar/preprocessed-dataset-sentiment-analysis). I had to do some tweaking to get it working as we expect.

#### Dependencies
In terms of dependencies,
we needed some external python modules which I have used extensively in this project.
`uvicorn` is used as a server,
`pytest` is used to have the unit tests done.

#### Implementation Details
First of all, we need the model to work as required. For that, I have managed a dataset that include all the needed labels such as `positive`, `negative` and `neutral`. As soon as I have found a suitable dataset I went to `Google Colab` to perform EDA and data preprocessing. With the help of `huggingface` `datasets` library I organized the data accordingly and initiated training. After training, as the moment I got the trained model, I hoped on the VS Code on my local machine and implemented the backend application.
You can check the `resource` directory above to have a look on how the training is done.