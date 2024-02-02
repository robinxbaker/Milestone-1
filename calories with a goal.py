def cals(goals_ans, plan_ans, assigned_ans, weight_ans, height_ans, age_ans, active_ans):
    if weight_ans[-3:] == "lbs":
        weight = int(weight_ans[:-3]) / 2.205
    else:
        weight = int(weight_ans[:-3])
    if height_ans[-2:] == "cm":
        height = int(height_ans[:-3])
    else:
        if height_ans[-2] == " ":
            feet = int(height_ans[:-2])
            inch = int(height_ans[-1])
        else:
            feet = int(height_ans[:-3])
            inch = int(height_ans[-2:])
        inch = feet * 12 + inch
        height = inch * 2.54
    if assigned_ans == "male":
        s = 5
    else:
        s = -151
    if active_ans == "none":
        activity = 1.2
    elif active_ans == "light":
        activity = 1.375
    elif active_ans == "moderate":
        activity = 1.55
    elif active_ans == "high":
        activity = 1.725
    else:
        activity = 1.9
    if goals_ans == "gain":
        mult = 1
    else:
        mult = -1
    if plan_ans == "one":
        amount = 500
    else:
        amount = 250
    return ((10 * weight + 6.25 * height - 5.0 * int(age_ans)) + s) * activity + mult * amount
    
lose_tip_info = "Most people find that increasing their activity levels helps with hunger, as it allows \
for someone to eat more and still be in a caloric deficit.\n\n\
A high protein moderate carb moderate diet is reccomended for weight loss, \
as protein is more satiating than carbs and fats.\n\n\
Try your best to get enough good quality sleep, as being sleep deprived will make \
you much more hungry than you would normally be.\n\n\
Stay away from processed foods, some examples being sugar, flour, candy, chocolate, bread, fried food, \
these kind of things. Basically, if you can't hunt it or grow it, don't eat it.\n\n\
Have your carbs be high in fiber, as fiber is very satiating.\n\n\
Avoid drinking your calories, as liquid calories digest faster, which leaves you hungry faster.\n"
gain_tip_info = "If you are having a hard time eating enough calories, consider making shakes \
with a lot of high calorie ingrediants. One such recipe is milk, oats, banans, peanut butter, and chocolate syrup. \
If you want to add more calories to the shake, adding 1 to 2 tbsp of olive oil will increase \
the calories by over 200 without adding much taste.\n"
incorrect = "I am sorry, that is an incorrect or unexpected response. Please type out \
a response exactly as given.\n"
welcome = "Welcome to Calories with a Goal, a FREE text-based program that provides you with a \
calorie amount tailored towards your fitness goals.\n\nNow with a macronutrient calculator!\n\n\
Please follow the prompts and respond to the questions asked by typing out a response that matches \
a selection given.\n\nLet us begin!\n"
science = "We as biological organisms need enery to function, and when it \
comes to our bodies, we refer to this energy as calories. Fat, or adipose tissue, as it is scientifically known, exists \
as a way to store calories for later use. Back when humans were hunter-gatherers, food \
was not nearly as common as it was today, so being able to store calories in the body for \
use during a famine was very beneficial. In our modern day, however, food is extremely easy to \
access. Because of this, humans often each more than we need. The body then takes these \
excess calories and stores them in the form of body fat. To access and burn these fat stores, \
we must be in a caloric deficit, meaning we must eat less calories than our body burns. If \
we do this, our body will make up for the calorie desparity by using stored body fat. Different \
foods can be considered healthier than others and can certainly influence how much we eat, \
but weight loss ultimately comes down to calories. If someone eats and absorbs more calories than \
their body uses, they will gain weight, and if someone eats less calories than their \
body uses, they will lose weight. Because of this, if someone is trying to gain or lose weight, \
it can be beneficial to calculate how many calories they need for this goal. That is where \
this program comes in.\n\n"
info = "One gram of fat is nine calories. One gram of carbohydrate is four calories. \
One gram of protein is four calories. One gram of alcohol is seven calories. In the US, \
most food comes with a nutrition label. This label will show how many calories that food has\
for a certain weight. For example, white rice has 3.75 calories per gram. You can use\
this nutrition label and a food scale to measure how much of a certain food has a certain amount\
of calories and use this to eat towards your specific calorie goal. It is possible to \
semi-accurately track calories without a food scale, but a food scale is HIGHLY recommended, \
especially if your goal is to lose weight.\n\n"
info_count_cals = "Would you like information on how to count calories? Only answer \
no if you have extensive knowlege and / or experience with counting calories.\n"
skip_to_macro_calc = "If you are already familiar with Calories with a Goal and would like to \
use the macronutrient calculator with an already-known calorie amount in mind, would you \
like to skip to the macronutrient calculator?\n"
goals = "If you make a wrong selection on accident or a selection that you would like \
changed later, you will be given the opportunity to do so.\n\nWe are going to start off with \
your bodyweight goals.\n\nWhen it comes to dieting, most people fall into one of two \
camps: losing weight or gaining weight.\n\nWhich one of these are you looking to do?\n"
assigned = "Now, we will gather biometic information to determine how many calories you should \
eat every day. All of these questions are asked because they strongly determine how many \
calories someone burns in a given day.\n\nWere you assigned female or male at birth? This is \
asked due to biological differences that, on average, affect how many calories someone burns in a day.\n"
weight = "What was your most recent weight?\n"
height = "What is your height?\n"
age = "What is your current age?\n"
active = "How active are you?\n"
would_you_like_macros = "Would you like to calculate how many macronutrients (protein, fat, carbohydrates\
) you should eat in a day? This is recommended to help adherence to the calorie amount if one's goal \
is to lose weight. Following specific amounts of macronutrients will require more selective food choices \
than just counting calories. This is completely optional.\n"
would_you_prefer = "Would you prefer to follow a low carb high fat, high carb low fat, moderate carb moderate fat, \
or high protein macronutrient ratio? High protein is recommended for fat loss, moderate carb moderate \
fat is recommended for weight gain.\n"
print(welcome)
name = input("Please start by entering your name.\n\n")
print(f"Welcome, {name}.\n\nBefore we begin, would you like the science of how weight loss and \
weight gain works? Knowledge is power, and having a further understanding of the science behind your goals \
may aide in sticking to a goal.\n")
science_ans = input("Type yes or no.\n\n")
if science_ans == "yes":
    print(science)
print(info_count_cals)
info_ans = input("Type yes or no.\n\n")
if info_ans == "yes":
    print(info)
print(skip_to_macro_calc)
skip_ans = input("Type yes or no.\n\n")
if skip_ans != "yes":
    print(goals)
    while True:
        goals_ans = input("Type lose for losing weight.\n\nType gain for gaining weight.\n\n")
        if goals_ans == "lose" or "gain":
            print(f"You have selected that you want to {goals_ans} weight.\n")
            break
        print(incorrect)
    print(f"Would you rather follow a plan that allows you to {goals_ans} one pound \
a week or one-half pound a week? For weight loss, one pound a week is faster, but \
most people find losing one-half pound a week noticably easier.\n")
    while True:
        plan_ans = input("Type one for one pound a week.\n\nType half for one-half pound a week.\n\n")
        if plan_ans == "one" or plan_ans == "half":
            print(f"You have selected that you want to {goals_ans} {plan_ans} pound a week.\n")
            break
        print(incorrect)
    print(assigned)
    while True:
        assigned_ans = input("Type male for male at birth.\n\nType female for female at birth.\n\n")
        if assigned_ans == "male" or "female":
            print(f"You have selected that you were assigned {assigned_ans} at birth.\n")
            break
        print(incorrect)
    print(weight)
    good = False
    while True:
        weight_ans = input("Please type a number followed by a space followed by kg to represent kilograms or lbs to \
represent pounds. Two examples: 110 lbs and 97 kg\n\n")
        for i in range(1, 7):
            try:
                if weight_ans[i] == " ":
                    if weight_ans[:i].isnumeric() and weight_ans[i + 1:] == "kg" or weight_ans[i + 1:] == "lbs":
                        good = True
                        break
            except IndexError:
                break
        if good:
            print(f"You have selected that your most recent weight is {weight_ans}.\n")
            break
        print(incorrect)
    print(height)
    good = False
    while True:
        height_ans = input("Please type a number followed by a space followed by cm to represent centimeters, or a number \
followed by a space followed by another number to represent feet and inches. Two examples: 156 cm, 5 9\n\n")
        for i in range(len(height_ans)):
            if height_ans[i] == " " \
                and height_ans[:i].isnumeric() \
                and ((height_ans[i + 1:].isnumeric() and (len(height_ans[i + 1:]) == 1 or len(height_ans[i + 1:]) == 2)) or height_ans[i + 1:] == "cm"):
                good = True
        if good:
            print(f"You have selected that your most recent height is {height_ans}\n")
            break
        print(incorrect)
    print(age)
    while True:
        age_ans = input("Type a number that represents your age in years.\n\n")
        if age_ans.isnumeric():
            if int(age_ans) > 0 and int(age_ans) < 120:
                print(f"You have selected that you are {age_ans} years of age.\n")
                break
        print(incorrect)
    print(active)
    while True:
        active_ans = input("Type none if you participate in little to no exercice.\n\n"
                           "Type light if you exercise one to three times a week.\n\n"
                           "Type moderate if you exercise four to five times a week.\n\n"
                           "Type high if you exercise every day or do intense exercise four to five times a week.\n\n"
                           "Type very high if you have a physical job that involves a lot of walking and if you work out at least three times a week.\n\n")
        if active_ans == "none" or active_ans == "light" or active_ans == "moderate" or active_ans == "high" or active_ans == "very high":
            break
        print(incorrect)
    print(f"Now to put it all together.\n\nYou want to {goals_ans} weight.\n")
    print(f"You want to {goals_ans} {plan_ans} pounds of bodyweight a week.\n\n"
            f"You were assigned {assigned_ans} at birth.\n\n"
            f"You weigh {weight_ans}.\n\n"
            f"Your height is {height_ans}.\n\n"
            f"You are {age_ans} years of age.\n\n"
            f"Your weekly activity is {active_ans}.\n\nIs all this correct?\n")
    correct = input("Type yes or no.\n\n")
    while True:
        if correct != "yes" and correct != "no":
            print(incorrect)
            correct = input("Type yes or no.\n\n")
        else:
            break
    if correct == "no":
        count = 0
        while True:
            print("Type goal to select a new goal.\n\n"
                "Type plan to select a new amount to lose or gain.\n\n"
                "Type sex to select if you were assigned male or female at birth.\n\n"
                "Type weight to select your weight.\n\n"
                "Type height to select your height.\n\n"
                "Type age to select your age.\n")
            new = input("Type activity to select your activity level.\n\n")
            if new == "goal":
                while True:
                    goals_ans = input("Type lose for losing weight.\n\nType gain for gaining weight.\n\n")
                    if goals_ans == "lose" or "gain":
                        break
                    print(incorrect)
            if new == "plan":
                while True:
                    plan_ans = input("Type one for one pound a week.\n\nType half for one-half pound a week.\n\n")
                    if plan_ans == "one" or "half":
                        break
                    print(incorrect)
            elif new == "sex":
                while True:
                    assigned_ans = input("Type male for male at birth.\n\nType female for female at birth.\n\n")
                    if assigned_ans == "male" or "female":
                        break
                    print(incorrect)
            elif new == "weight":
                good = False
                while True:
                    weight_ans = input("Please type a number followed by a space followed by kg to represent kilograms or lbs to represent pounds. Two examples: 110 lbs and 97 kg")
                    for i in range(1, 7):
                        try:
                            if weight_ans[i] == " ":
                                if weight_ans[:i].isnumeric() and weight_ans[i + 1:] == "kg" or weight_ans[i + 1:] == "lbs":
                                    good = True
                                    break
                        except IndexError:
                            break
                    if good:
                        break
                    print(incorrect)
            elif new == "height":
                good = False
                while True:
                    height_ans = input("Pleasetype a number followed by a space followed by cm to represent centimeters, or a number \
followed by a space followed by another number to represent feet and inches. Two examples: 156 cm, 5 9\n\n")
                    for i in range(1, 6):
                        try:
                            if len(height_ans) > 4:
                                if height_ans[:-3].isnumeric() and height[-3] == " " and height_ans[-2:] == "cm":
                                    good = True
                                    break
                            elif len(height_ans) > 4:
                                if (height_ans[-1].isnumeric() and height_ans[-2] == " " and height_ans[:-2].isnumeric()) or \
                                    (height_ans[-2:].isnumeric() and height_ans[-3] == " " and height_ans[:-3].isnumeric()):
                                    good = True
                                    break
                            elif len(height_ans) > 3:
                                if height_ans[-1].isnumeric() and height_ans[-2] == " " and height_ans[:-2].isnumeric():
                                    good = True
                                    break
                        except IndexError:
                            break
                    if good:
                        break
                    print(incorrect)
            elif new == "age":
                while True:
                    age_ans = input("Type a number that represents your age in years.\n\n")
                    if age_ans.isnumeric():
                        if int(age_ans) > 0 and int(age_ans) < 120:
                            break
                    print(incorrect)
            elif new == "activity":
                while True:
                    active_ans = input("Type none if you participate in little to no exercice.\n\n"
                                        "Type light if you exercise one to three times a week.\n\n"
                                        "Type moderate if you exercise four to five times a week.\n\n"
                                        "Type high if you exercise every day or do intense exercise four to five times a week.\n\n"
                                        "Type very high if you have a physical job that involves a lot of walking and if you work out at least three times a week.\n\n")
                    if active_ans == "none" or active_ans == "light" or active_ans == "moderate" or active_ans == "high" or active_ans == "very high":
                        break
                    print(incorrect)
            else:
                print(incorrect)
                count -= 1
            count += 1
            print(f"You want to {goals_ans} weight.\n")
            print(f"You want to {goals_ans} {plan_ans} pounds of bodyweight a week.\n\n"
                    f"You were assigned {assigned_ans} at birth.\n\n"
                    f"You weigh {weight_ans}.\n\n"
                    f"Your height is {height_ans}.\n\n"
                    f"You are {age_ans} years of age.\n\n"
                    f"Your weekly activity is {active_ans}.\n\nIs all this correct?\n")
            correct = input("Type yes or no.\n\n")
            joshy = False
            while True:
                if correct != "yes" and correct != "no":
                    print(incorrect)
                    correct = input("Type yes or no.\n\n")
                else:
                    break
            if correct == "yes":
                break
            else:
                while True:
                    print("You have been changing values more times than expected. Are you sure you want to do this?\n")
                    sure = input("Type yes or no.\n\n")
                    if sure != "yes" and sure != "no":
                        print(incorrect)
                    elif sure == "no":
                        joshy = True
                    break
            if correct == "yes" or joshy:
                break
    calories = cals(goals_ans, plan_ans, assigned_ans, weight_ans, height_ans, age_ans, active_ans) // 1
    print(calories)
    print(f"\nThis is the amount of calories you should eat in a day to {goals_ans} {plan_ans} pound of bodyweight a week.\n")
    print("Would you like tips on how to make sticking to your calorie amount easier?\n")
    while True:
        tips = input("Type yes or no.\n\n")
        if tips == "yes":
            if goals_ans == "lose":
                print(lose_tip_info)
            else:
                print(gain_tip_info)
            break
        elif tips == "no":
            break
        print(incorrect)
    print(would_you_like_macros)
    while True:
        macro_ans = input("Type yes or no.\n\n")
        if macro_ans == "yes":
            print(would_you_prefer)
            while True:
                calories = int(calories)
                prefer_ans = input("Type fat for a high fat low carb diet, carb "
                                    "for a high carb low fat diet, protein for a high "
                                    "protein diet, or moderate for a more "
                                    "balanced approach.\n\n")
                protein = calories * 0.333
                if prefer_ans == "moderate":
                    carb = calories * 0.333
                    fat = calories * 0.333
                    break
                if prefer_ans == "fat":
                    carb = calories * 0.166
                    fat = calories * 0.5
                    break
                if prefer_ans == "carb":
                    carb = calories * 0.5
                    fat = calories * 0.166
                    break
                if prefer_ans == "protein":
                    protein = calories * 0.5
                    fat = calories * 0.25
                    carb = calories * 0.25
                    break
                else:
                    print(incorrect)
            print(f"{protein} calories protein, {fat} calories fat, {carb} calories carbs.\n")
            print("This is how many calories of each macronutrient to eat for your selected ratio.\n")
            break
        elif macro_ans == "no":
            break
        else:
            print(incorrect)
    print("Thank you for using Calories with a Goal, and good luck!") 
else:
    print("You have chosen to skip to finding a macronutrient ratio and amount for a certain amount of calories.\n\n")
    while True:
        calories = input("Please enter a number representing the amount of calories you would like to use.\n\n")
        if calories.isnumeric():
            break
        else:
            print(incorrect)
    print(f"You have entered {calories} calories.\n\n")
    print(would_you_prefer)
    while True:
        calories = int(calories)
        prefer_ans = input("Type fat for a high fat low carb diet, carb "
                            "for a high carb low fat diet, protein for a high "
                            "protein diet, or moderate for a more "
                            "balanced approach.\n\n")
        protein = calories * 0.333
        if prefer_ans == "moderate":
            carb = calories * 0.333
            fat = calories * 0.333
            break
        if prefer_ans == "fat":
            carb = calories * 0.166
            fat = calories * 0.5
            break
        if prefer_ans == "carb":
            carb = calories * 0.5
            fat = calories * 0.166
            break
        if prefer_ans == "protein":
            protein = calories * 0.5
            fat = calories * 0.25
            carb = calories * 0.25
            break
        else:
            print(incorrect)
    print(f"{protein} calories protein, {fat} calories fat, {carb} calories carbs.\n\n")
    print("This is how many calories of each macronutrient to eat for your selected ratio.\n\n")
    print("Thank you for using Calories with a Goal, and good luck!")