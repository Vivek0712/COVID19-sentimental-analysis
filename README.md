# COVID19-sentimental-analysis
Analysing the sentiment of people during each phase of COVID-19 Pandemic in India
Blog: https://vivekraja98.medium.com/detecting-and-visualizing-twitter-sentiment-during-covid-19-pandemic-using-aws-comprehend-and-c641e1549e2b


## Tweet Processing and Upload

The tweets were collected on three bases: 1. Keyword, 2. Location 3. Date range. Only tweets in English were collected for this purpose
Keyword: 15 trending keywords related to COVID-19.
Location: Chennai, Bangalore, Hyderabad, Delhi, Mumbai, Kolkata.
Date Range: Three phases — Pre-lockdown, Lockdown, Unlock.
The GetOldTweets3 python library was used to collect the tweets based on the above three criteria. To preprocess the data, NLTK packages were used.
To save you from the hassle, I have uploaded the dataset in my Github repo. The techniques used for data collection and preprocessing is explained in the readme file.
All dataset contains three features: tweet text, location, phase.
https://github.com/Vivek0712/covidtwitterdataset

## Results

![1*kPp2FRpR2I4TZ24AHjyaKQ](https://user-images.githubusercontent.com/25385071/114313953-51451600-9b16-11eb-961e-9fae583652ba.png)
![1*lpxrEAlmdwElLxAIm_kH6A](https://user-images.githubusercontent.com/25385071/114313990-7b96d380-9b16-11eb-90ff-12f5b724a69b.png)
