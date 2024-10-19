import pandas as pd

df=pd.read_csv("C:\\Users\\Ataullah Shaikh\\Downloads\\CAR DETAILS FROM CAR DEKHO.csv",delimiter=',')
df=pd.DataFrame(df)

# Here define function where all the variable consist
def filter_cars(df, Name_of_Car=None,min_price=None,max_price=None,Fuel=None,Seller_type=None,Transmission=None,Owner=None,Year=None,Km_driven=None):
    
    # Copy all data to a variable where varable name is filtered data 
    filtered_df = df.copy()
    
    # Apply filters based on user input
    if Name_of_Car:
           filtered_df = filtered_df[filtered_df['Name_of_Car'].str.lower()==Name_of_Car.lower()]
     
    # We use 'is not None' because you will have to provide value of this type of variable, It's manadatory to provide input
    if min_price is not None:
           filtered_df = filtered_df[filtered_df['Selling_price'] >= min_price]
    if max_price is not None:
           filtered_df = filtered_df[filtered_df['Selling_price'] <= max_price]
        
        # we  don't  use 'is not None' because this value is optional 
    if Fuel:
           filtered_df = filtered_df[filtered_df['Fuel'].str.lower()==Fuel.lower()]
    
    if Seller_type:
           filtered_df=filtered_df[filtered_df['Seller_type'] ==Seller_type]
    
    if Transmission:
           filtered_df=filtered_df[filtered_df['Transmission'].str.lower() ==Transmission.lower()]
    
    if Owner:
           filtered_df=filtered_df[filtered_df['Owner'].str.lower()==Owner.lower()]

    if Year is not None:
           filtered_df=filtered_df[filtered_df['Year']==Year]
        
    if Km_driven is not None:
           filtered_df=filtered_df[filtered_df['Km_driven']<=Km_driven]          
    return filtered_df 
# Taking input from user: 

Name_of_Car=input("Enter Name of Car(or leave blank): ")
min_price=int(input("Enter the min price of car(This is manadatory to provide): "))
max_price=int(input("Enter the maximum price of car(This is manadatory to provide): "))
Fuel=input("Choose Fule type(Petrol/Diesel/CNG)(or leave blank): ")
Seller_type=input("Enter seller type(Individual/Dealer)(or leave blank): ")
Transmission=input("Enter transmission mode(Automatic/Manual)(or leave blank): ")
Owner=input("Enter type of Owner(First/Second so on... )(or leave blank): ")
Year=int(input("Enter Model Year of Car(This is manadatory to provide): "))
Km_driven=int(input("Enter Km_driven(This is manadatory to provide): "))

# Calling the function now 
Result=filter_cars(df,Name_of_Car= Name_of_Car, min_price=min_price, max_price=max_price,Fuel=Fuel,Seller_type=Seller_type,Transmission=Transmission,Owner=Owner,Year=Year,Km_driven=Km_driven)
print("Here is your match:\n ",Result)

# Save the filtered results to a CSV file

Result.to_csv("C:\\Users\\Ataullah Shaikh\\OneDrive\\Desktop\\Result_of_Filtererde_data.csv", index=False)
