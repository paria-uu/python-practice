Math_Score = 100
Physics_Score = 85
Chemistry_Score = 100

if Physics_Score > 85 and Math_Score > 90:
    print('You have been accepted into the Computer Engineering program.')

elif Chemistry_Score > 95 and Physics_Score > 80:
    print('You have been accepted into the Computer Engineering program.')

elif Chemistry_Score + Physics_Score + Math_Score <= 240:
    print('You have not been accepted.')

else:
    print('You have not been accepted into the Computer Engineering program.')
