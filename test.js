const fs = require('fs');

// Mock localStorage and window
global.localStorage = {
  data: {},
  setItem(key, val) { this.data[key] = val; },
  getItem(key) { return this.data[key] || null; },
  removeItem(key) { delete this.data[key]; }
};
global.window = {};

// Load code
const dataCode = fs.readFileSync('./js/data.js', 'utf8');
const appCode = fs.readFileSync('./js/app.js', 'utf8');
eval(dataCode);
eval(appCode);

window.App.saveSelectedCareer('software-developer');

// Test Case 1: All 0s
console.log('Test Case 1: All 0s');
window.App.saveRatings({});
let result = window.App.analyze();
console.log('Match Percentage:', result.matchPercentage);
console.log('Productivity Score:', result.productivityScore);
console.log('Missing count:', result.missing.length);
console.log('Roadmap length:', result.roadmap.length);

// Test Case 2: All 5s
console.log('\nTest Case 2: All 5s');
let ratings = {};
window.AppData.careers[0].skills.forEach(s => ratings[s.id] = 5);
window.App.saveRatings(ratings);
result = window.App.analyze();
console.log('Match Percentage:', result.matchPercentage);
console.log('Productivity Score:', result.productivityScore);
console.log('Missing count:', result.missing.length);
console.log('Roadmap length:', result.roadmap.length);
console.log('Strong count:', result.strong.length);

