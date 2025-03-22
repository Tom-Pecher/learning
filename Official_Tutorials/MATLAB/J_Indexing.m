
% MATLAB: MathWorks, OnRamp
% Section 9: Indexing

data = rand(4, 7)

% We can index matrices to access specific elements:
data(3, 5)

% Index first element:
data(1, 1)

% Index last element:
data(end, end)

% Index a range of elements:
data(2:3, 4:6)

% Index all elements in a row or column:
data(2, :)
data(:, 3)
