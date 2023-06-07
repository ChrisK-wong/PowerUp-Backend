# PowerUp Backend

## Using the API

API: [power-up-backend.vercel.app](power-up-backend.vercel.app)

## Recommendations

### foods
| Endpoint   | HTML Parameters | Returns | Sample Request |
|------------|-----------------|---------|----------------|
| /api/foods/{type}<br><br/>types:<br><br/>`calorie`<br/>`protein`<br/>`carbs`<br/>`fiber`<br/>`fat`| min: int<br>max: int<br>limit: int | Returns JSON list of foods and nutritional information given the parameters | https://power-up-backend.vercel.app/api/foods/calories?min=100&max=200&limit=1 |

### exercise
| Endpoint   | HTML Parameters | Returns                                                | Sample Request |
|------------|-----------------|--------------------------------------------------------|----------------|
| /api/exercise/{type}<br><br/>types:<br><br/>`cardio`<br/>`flexibility`<br/>`arms`<br/>`core`<br/>`legs` | limit: int      | Returns JSON list of exercise obj relating to the type | https://power-up-backend.vercel.app/api/foods/calories?min=100&max=200&limit=1 |

## Scoring

### health score
| Endpoint   | HTML Parameters | Returns                                               | Sample Request |
|------------|-----------------|-------------------------------------------------------|----------------|
| /api/score/health | gender: int<br/>height: int<br/>weight: int | <pre lang="json">{&#13;    "health_score": 0.8&#13;}</pre> | [https://power-up-backend.vercel.app/api/score/health?gender=0&height=180&weight=60](https://power-up-backend.vercel.app/api/score/health?gender=0&height=180&weight=60) |

#### fitness score
| Endpoint   | HTML Parameters | Returns  | Sample Request |
|------------|-----------------|----------|----------------|
| /api/score/fitness | heart_rate: int<br/>active_calories: int<br/>steps: int | <pre lang="json">{&#13;    "fitness_score": 0.65&#13;}</pre> | [https://power-up-backend.vercel.app/api/score/fitness?heart_rate=80&active_calories=100&steps=3000](https://power-up-backend.vercel.app/api/score/fitness?heart_rate=80&active_calories=100&steps=3000) |

#### sleep score
| Endpoint   | HTML Parameters | Returns | Sample Request |
|------------|-----------------|---------|----------------|
| /api/score/sleep | gender: int<br/>health_score: float<br/>fitness_score: float<br/>average_sleep_hours: int | <pre lang="json">{&#13;    "sleep_score": 0.74&#13;}</pre> | [https://power-up-backend.vercel.app/api/score/sleep?gender=0&health_score=0.8&fitness_score=0.8&average_sleep_hours=6](https://power-up-backend.vercel.app/api/score/sleep?gender=0&health_score=0.8&fitness_score=0.8&average_sleep_hours=6) |

#### diet score
| Endpoint   | HTML Parameters | Returns | Sample Request |
|------------|-----------------|---------|----------------|
| /api/score/diet | times_eating_out: int<br/>times_eating_vegetables: int | <pre lang="json">{&#13;    "diet_score": 0.57&#13;}</pre> | [https://power-up-backend.vercel.app/api/score/diet?times_eating_out=2&times_eating_vegetables=8](https://power-up-backend.vercel.app/api/score/diet?times_eating_out=2&times_eating_vegetables=8) |

#### exercise score
| Endpoint   | HTML Parameters | Returns  | Sample Request |
|------------|-----------------|----------|----------------|
| /api/score/exercise | workouts_per_week: int<br/>workout_intensity: string | <pre lang="json">{&#13;    "diet_score": 1.0&#13;} | [https://power-up-backend.vercel.app/api/score/exercise?workouts_per_week=5&workout_intensity=3](https://power-up-backend.vercel.app/api/score/exercise?workouts_per_week=5&workout_intensity=3) |

 #### overall score
| Endpoint   | HTML Parameters | Returns  | Sample Request |
|------------|-----------------|----------|----------------|
| /api/score/overall | health_score: float<br/>fitness_score: float<br/>sleep_score: float<br/>diet_score: float<br/>exercise_score: float |  <pre lang="json">{&#13;    "diet_score": 890.0&#13;} | [Sample Request](https://power-up-backend.vercel.app/api/score/overall?health_score=0.8&fitness_score=0.9&sleep_score=0.7&diet_score=0.85&exercise_score=0.95) |

<!--
#### all scores
| Endpoint   | HTML Parameters | Returns  | Sample Request |
|------------|-----------------|----------|----------------|
| /api/score/all | gender: int<br/>height: int<br/>weight: int<br/>heart_rate: int<br/>active_calories: int<br/>steps: int<br/>average_sleep_hours: int<br/>times_eating_out: int<br/>times_eating_vegetables: int<br/>workouts_per_week: int<br/>workout_intensity: string | {"health_score": 0.8, "fitness_score": 0.9, "sleep_score": 0.7, "diet_score": 0.85, "exercise_score": 0.95, "overall_score": 0.88} | [Sample Request](https://power-up-backend.vercel.app/api/score/all?gender=0&height=180&weight=60&heart_rate=72&active_calories=500&steps=10000&average_sleep_hours=8&times_eating_out=2&times_eating_vegetables=5&workouts_per_week=5&workout_intensity=high) |
Just replace Sample Request with actual URLs for your API endpoints. -->






