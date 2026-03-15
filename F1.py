import fastf1

# Voorbeeld: Laad data voor een race
session = fastf1.get_session(2023, 'Monaco', 'R')
session.load()

# Print de resultaten
print(session.results)

#start