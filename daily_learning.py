
from random import choice, choices


LEARNING_TOPICS = {
    'C'              :  7,
    'C++'            :  10,
    'C#'             :  6,
    'DOCKERFILE'     :  3,
    'GIT'            :  10,
    'FLUTTER'        :  2,
    'GRAPHQL'        :  1,
    'GOLANG'         :  4,
    'HTML/CSS'       :  10,
    'JAVA'           :  5,
    'JAVASCRIPT'     :  4,
    'JULIA'          :  1,
    'MATLAB'         :  4,
    'NOSQL'          :  3,
    'PHP'            :  2,
    'PYTHON'         :  10,
    'R'              :  6,
    'RESTFUl'        :  1,
    'RUBY'           :  1,
    'RUST'           :  7,
    'SCALA'          :  1,
    'SHELLSCRIPT'    :  7,
    'SQL'            :  5,
    'TERRAFORM'      :  2,
    'TYPESCRIPT'     :  3,
    'WOLFRAM'        :  9,
    'YAML'           :  3
}
learning_selection = choices(tuple(LEARNING_TOPICS.keys()), tuple(LEARNING_TOPICS.values()), k=1)[0]
print('LEARNING:')
print(f'Your daily topic is "{learning_selection}"!')



TEMPLATES_LANGUAGES = [
    'C',
    'C++',
    'C#',
    'GOLANG',
    'JAVA',
    'JAVASCRIPT',
    'PHP',
    'PYTHON',
    'RUST',
    'WOLFRAM'
]

DATA_STRUCTURES = [
    'ARRAYS',
    'GRAPHS',
    'LINKED LISTS',
    'STACKS',
    'TREES',
    'QUEUES'
]
SEARCH_ALGORITHMS = [
    'BINARY SEARCH',
    'EXPONENTIAL SEARCH',
    'INTERPOLATION SEARCH',
    'JUMP SEARCH',
    'LINEAR SEARCH',
    'TERNARY SEARCH'
]
SORTING_ALGORITHMS = [
    'BUBBLE SORT',
    'COUNTING SORT',
    'HEAP SORT',
    'INSERTION SORT',
    'MERGE SORT',
    'RADIX SORT',
    'SELECTION SORT',
    'SHELL SORT',
    'QUICK SORT'
]

all_template_tasks = DATA_STRUCTURES + SEARCH_ALGORITHMS + SORTING_ALGORITHMS
exercise_selection = choices(all_template_tasks)
language_selection = choices(TEMPLATES_LANGUAGES)
print('LEARNING:')
print(f'Your daily exercise is "{exercise_selection}" in "{language_selection}"!')



ML_ALGORITHMS = [
    'ANN',
    'AUTOENCODER',
    'BOLTZMANN MACHINE'
    'CNN',
    'DBSCAN',
    'GAN',
    'GMM',
    'K-MEANS CLUSTERING',
    'KNN',
    'PCA',
    'RNN',
    'TRANSFORMER'
]

ml_exercise_selection = choices(ML_ALGORITHMS)
language_selection = choices(TEMPLATES_LANGUAGES)
print('LEARNING:')
print(f'Your daily exercise is "{ml_exercise_selection}" in "{language_selection}"!')