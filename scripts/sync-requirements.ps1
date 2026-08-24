[CmdletBinding()]
param()

$repoRoot = Split-Path -Parent $PSScriptRoot
$env:UV_CACHE_DIR = Join-Path $repoRoot ".uv-cache"

Push-Location $repoRoot
try {
    & uv export `
        --format requirements.txt `
        --frozen `
        --no-hashes `
        --no-header `
        --no-annotate `
        --no-emit-project `
        -o requirements.txt

    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}
finally {
    Pop-Location
}
