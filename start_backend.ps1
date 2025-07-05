# PowerShell script to start the Flask backend automatically
Write-Host "Starting Flask backend with auto-reload..." -ForegroundColor Green
Set-Location backend

# Check if virtual environment exists
if (Test-Path "venv\Scripts\activate") {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & "venv\Scripts\activate"
    
    # Check if required packages are installed
    Write-Host "Checking dependencies..." -ForegroundColor Yellow
    python -c "import flask, flask_cors" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Installing missing dependencies..." -ForegroundColor Yellow
        pip install flask flask-cors
    }
    
    Write-Host "Starting Flask app with auto-reload..." -ForegroundColor Green
    python app.py
} else {
    Write-Host "Error: Virtual environment not found. Please create it first." -ForegroundColor Red
    Write-Host "Run: python -m venv venv" -ForegroundColor Yellow
} 