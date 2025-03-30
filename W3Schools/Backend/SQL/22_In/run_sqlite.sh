
DB_NAME="example.db"

echo "Setting up database..."
sqlite3 $DB_NAME < setup.sql

echo "Running queries..."
echo ""

sqlite3 $DB_NAME < queries.sql

echo ""

# echo "🔹 Tearing down database..."
# sqlite3 $DB_NAME < teardown.sql

echo "All steps completed!"
