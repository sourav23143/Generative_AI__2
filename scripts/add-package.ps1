[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory = $true, Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$Packages,

    [switch]$Dev,

    [ValidateSet("lower", "major", "minor", "exact")]
    [string]$Bounds = "lower"
)

$repoRoot = Split-Path -Parent $PSScriptRoot
$env:UV_CACHE_DIR = Join-Path $repoRoot ".uv-cache"

Push-Location $repoRoot
try {
    $addArgs = @("add")

    if ($Dev) {
        $addArgs += "--dev"
    }

    if ($Bounds) {
        $addArgs += "--bounds"
        $addArgs += $Bounds
    }

    $addArgs += $Packages

    $commandPreview = "uv " + ($addArgs -join " ")
    if ($PSCmdlet.ShouldProcess(($Packages -join ", "), $commandPreview)) {
        & uv @addArgs
        if ($LASTEXITCODE -ne 0) {
            exit $LASTEXITCODE
        }

        & (Join-Path $PSScriptRoot "sync-requirements.ps1")
        if ($LASTEXITCODE -ne 0) {
            exit $LASTEXITCODE
        }
    }
}
finally {
    Pop-Location
}
