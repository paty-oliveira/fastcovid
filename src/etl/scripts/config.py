from pyspark.sql.types import IntegerType, DateType, FloatType

DATASET_PATH = 'raw_data/covid-19-world-cases-deaths-testing.csv'

TARGET_PATH = 'transformed_data/transformed_covid_world_cases.csv'

DATA_TYPES = {'date': DateType(),
              'new_cases': IntegerType(),
              'new_deaths': IntegerType(),
              'new_tests': IntegerType(),
              'total_cases': IntegerType(),
              'total_deaths': IntegerType(),
              'total_tests': IntegerType(),
              'icu_patients': IntegerType(),
              'hosp_patients': IntegerType(),
              'total_vaccinations': IntegerType(),
              'population': IntegerType(),
              'median_age': FloatType(),
              'gdp_per_capita': FloatType(),
              'cardiovasc_death_rate': FloatType(),
              'diabetes_prevalence': FloatType(),
              'female_smokers': FloatType(),
              'male_smokers': FloatType(),
              'life_expectancy': FloatType()
              }

MISSING_VALUES = {'new_cases': 0,
                  'new_deaths': 0,
                  'new_tests': 0,
                  'total_cases': 0,
                  'total_deaths': 0,
                  'total_tests': 0,
                  'icu_patients': 0,
                  'hosp_patients': 0,
                  'weekly_icu_admissions': 0,
                  'weekly_hosp_admissions': 0,
                  'total_vaccinations': 0,
                  'female_smokers': 0,
                  'male_smokers': 0
                  }

COLUMNS_TO_SELECT = ['iso_code',
                     'continent',
                     'location',
                     'date',
                     'new_cases',
                     'new_deaths',
                     'new_tests',
                     'total_cases',
                     'total_deaths',
                     'total_tests',
                     'icu_patients',
                     'hosp_patients',
                     'weekly_icu_admissions',
                     'weekly_hosp_admissions',
                     'total_vaccinations',
                     'population',
                     'median_age',
                     'gdp_per_capita',
                     'cardiovasc_death_rate',
                     'diabetes_prevalence',
                     'female_smokers',
                     'male_smokers',
                     'life_expectancy']
