# Krshak-Saathee
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <b>A simple ML based website which determines the demand, price and yield prediction, Crop Recommendation and fertizers recommendation for the selected crops. </b>
    <br>
    <b>This project was created during the convergence fest of VNRVJIET as part of the software hackathon event conducted by the institute. The team members and conributors for the project are : </b>
    <!-- add github ahref -->
    <ol>
        <a href="https://github.com/ritish1082"><li>M.Sai Ritish Reddy</li></a>
        <li>M. Harikesh</li>
        <li>G. Hemanth Verma</li>
        <li>Santosh</li>
    </ol>
    <hr>
    <h1>Technologies Used</h1>
    <ol>
        <li>Ml Models</li>
        <ul>
            <li>Linear Regression</li>
            <li>Decision Tree Classifier</li>
        </ul>
        <li>Technologies </li>
        <ul>
            <li>Html 5</li>
            <li>CSS</li>
            <li>Bootstrap 5</li>
            <li>Flask</li>
            <li>Python Modules</li>
            <ol>
                <li>Sckit-learn</li>
                <li>Numpy</li>
                <li>Pandas</li>
                <li>Matplotlib</li>
            </ol>
        </ul>
    </ol>
    <hr>
    <h1>How To Use</h1>
    <p>There are mainly 5 features regardig the above project which include demand prediction, price and yield prediction, Crop Recommendation and fertizers recommendation for the selected crops.</p>
    <h2>Crop Registration</h2>
    <p>The farmer who has decide to grow a particular crop in a particular crop season registers himself using the crop registration portal present in the main homepafe oft the website.The farmer has to fill in certaiin details such as:
        <ol>
            <li>District</li>
            <li>Crop</li>
            <li>Area</li>
        </ol>
        Upon registration the user recieves a successful registration message and go back to the home page for further operations.
    </p>
    <h2>Crop Statistics</h2>
    <p>In this functionality the user can get the expected demand of the particular crop choosen and the number of people who have already registered for the cultivation of the crop at that particular crop season.The user has to fill in details like:
        <ol>
            <li>Crop</li>
        </ol> The user gets a barplot in return to the input given.</p>
     <h2>Crop Yield Statistics</h2>
     <p>The user can find out the yield and the price they would get upon cultivating a certain area of crop.The user has to fill in the following details:
         <ol>
             <li>District</li>
             <li>Crop</li>
             <li>Planned area of cultivation(in acres)</li>
         </ol>
        </p>
    <h2>Crop Recommendation</h2>
    <p>The user gets recommendation on crop variety suitable to the soil profile of their land.The user has to fill in the following details:
        <ol>
            <li>N,P,K values</li>
            <li>Temperature(mean temp. in your area)</li>
            <li>PH Value</li>
            <li>Rain(mean rainfall in your area)</li>
            <li>Humidity</li>
        </ol>
        A recommended crop suitable for your soil profile is returned.
    </p>
    <h2>Fertizers Recommendation</h2>
    <p>The user gets recommendation on which fertilizers to apply on the crop to enhance production.The user has to fill in the following details:
        <ol>
            <li>Crop</li>
            <li>N,P,K Values</li>
            <li>Temperature(mean temp. in your area)</li>
            <li>Humidity</li>
            <li>Moisture Content</li>
        </ol>
        A recommended fertilizer suitable for your soil profile and crop is returned.
    </p>
    <h2>Further Scope</h2>
    <ol>
        <li>The above performed recommendation models can be integrated with IOT based bluetooth modeules which can depict the N, P, K, temperature, humidity, moisture content values from the soil itself by using sensors. </li>
        <li>More data can be collected manually via web scrapping to make the system more accurate </li>
    </ol>
</body>
</html>
