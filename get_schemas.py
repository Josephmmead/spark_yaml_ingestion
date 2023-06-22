from pyspark.sql.types import StructField, StringType, StructType, IntegerType, DecimalType, DateType, DoubleType

def get_schema():
    schema_dict = {}

    customer_schema = StructType([StructField('customer', StringType(), False),
                                  StructField('customer_id', StringType(), False)])
    
    transaction_schema = StructType([StructField('customer_id', StringType(), False),
                                     StructField('transaction_id', IntegerType(), False),
                                     StructField('transaction_amount', DecimalType(18,2), False)])
    
    demographic_schema = StructType([StructField('customer', StringType(), False),
                                      StructField('customer_id', StringType(), False),
                                      StructField('gender', StringType(), True),
                                      StructField('age', IntegerType(), True),
                                      StructField('country', StringType(), False),
                                      StructField('state', StringType(), False),
                                      StructField('salary', DecimalType(), False)])
    
    customer_demographics_schema = StructType([StructField("CustomerID", IntegerType(), nullable=False),
                                                StructField("FirstName", StringType(), nullable=True),
                                                StructField("LastName", StringType(), nullable=True),
                                                StructField("Gender", StringType(), nullable=True),
                                                StructField("Age", IntegerType(), nullable=True),
                                                StructField("DateOfBirth", DateType(), nullable=True),
                                                StructField("Email", StringType(), nullable=True),
                                                StructField("Phone", StringType(), nullable=True),
                                                StructField("AddressLine1", StringType(), nullable=True),
                                                StructField("AddressLine2", StringType(), nullable=True),
                                                StructField("City", StringType(), nullable=True),
                                                StructField("State", StringType(), nullable=True),
                                                StructField("ZipCode", IntegerType(), nullable=True),
                                                StructField("Country", StringType(), nullable=True),
                                                StructField("Nationality", StringType(), nullable=True),
                                                StructField("EducationLevel", StringType(), nullable=True),
                                                StructField("Occupation", StringType(), nullable=True),
                                                StructField("Income", IntegerType(), nullable=True),
                                                StructField("MaritalStatus", StringType(), nullable=True),
                                                StructField("NumberOfChildren", IntegerType(), nullable=True),
                                                StructField("LanguagePreference", StringType(), nullable=True),
                                                StructField("PreferredContactMethod", StringType(), nullable=True),
                                                StructField("LastPurchaseDate", DateType(), nullable=True),
                                                StructField("TotalPurchaseAmount", DoubleType(), nullable=True),
                                                StructField("LastLoginDate", DateType(), nullable=True),
                                                StructField("AccountCreateDate", DateType(), nullable=True),
                                                StructField("AccountType", StringType(), nullable=True),
                                                StructField("SubscriptionStatus", StringType(), nullable=True),
                                                StructField("PreferredPaymentMethod", StringType(), nullable=True),
                                                StructField("CreditScore", IntegerType(), nullable=True),
                                                StructField("CreditLimit", IntegerType(), nullable=True),
                                                StructField("MembershipTier", StringType(), nullable=True),
                                                StructField("LoyaltyPoints", IntegerType(), nullable=True),
                                                StructField("ReferralSource", StringType(), nullable=True),
                                                StructField("PurchaseFrequency", StringType(), nullable=True),
                                                StructField("FavoriteProductCategory", StringType(), nullable=True),
                                                StructField("PreferredStoreLocation", StringType(), nullable=True),
                                                StructField("TravelFrequency", StringType(), nullable=True),
                                                StructField("VehicleType", StringType(), nullable=True),
                                                StructField("InsuranceProvider", StringType(), nullable=True),
                                                StructField("HealthCondition", StringType(), nullable=True),
                                                StructField("SocialMediaUsage", StringType(), nullable=True),
                                                StructField("Interests", StringType(), nullable=True),
                                                StructField("SportsPreference", StringType(), nullable=True),
                                                StructField("MusicPreference", StringType(), nullable=True)])
    schema_dict['customer_schema'] = customer_schema
    schema_dict['transaction_schema'] = transaction_schema
    schema_dict['demographic_schema'] = demographic_schema
    schema_dict['customer_demographics_schema'] = customer_demographics_schema

    return schema_dict

