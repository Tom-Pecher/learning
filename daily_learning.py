
from random import choices


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