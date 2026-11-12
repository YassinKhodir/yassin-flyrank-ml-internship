'use strict';
// This calculator runs in the browser. It makes no network requests.
function calculateCTR(clicks, impressions) {
  if (!Number.isSafeInteger(clicks) || !Number.isSafeInteger(impressions) || clicks < 0 || impressions < 0) {
    return 'Enter whole, non-negative event counts within the safe number range.';
  }
  if (impressions === 0) return 'CTR cannot be calculated because impressions are zero.';
  const rate = clicks / impressions * 100;
  return `${clicks} ÷ ${impressions} × 100 = ${Number(rate.toFixed(4))}% CTR. A benchmark is needed to judge performance.`;
}
const form = typeof document === 'undefined' ? null : document.getElementById('ctr-form');
if (form) form.addEventListener('submit', function(event) {
  event.preventDefault();
  const clicksText = document.getElementById('clicks').value.trim();
  const impressionsText = document.getElementById('impressions').value.trim();
  const result = document.getElementById('ctr-result');
  result.textContent = !clicksText || !impressionsText ? 'Enter both clicks and impressions.' : calculateCTR(Number(clicksText), Number(impressionsText));
});
if (typeof module !== 'undefined') module.exports = { calculateCTR };
