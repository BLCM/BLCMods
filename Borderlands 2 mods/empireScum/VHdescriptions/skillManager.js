var mousedownbegin;
var lastTouched;
var touchtimer;

function handleMousedown(event) {
	event.preventDefault();
	switch (event.which) {
		case 1: //left mouse button
			window.clearTimeout(touchtimer);
			mousedownbegin = (new Date()).getTime();
			lastTouched = $(this);
			touchtimer = window.setTimeout('checkLongTouch(true)',500);
			break;
//		case 2: //middle mouse button
//			break;
//		case 3: //right mouse button
//			break;
	}
}
function handleMouseup(event) {
	event.preventDefault();
	switch (event.which) {
		case 1: //left mouse button
			window.clearTimeout(touchtimer);
			checkLongTouch(false);
			break;
		case 3: //right mouse button
			updatePoints($(this), -1);
			break;
	}
}

function checkLongTouch(fromTimer) {
	if (lastTouched !== null) {
		if (fromTimer === true) {
			updatePoints(lastTouched, -1);
			updatePoints(lastTouched, -1);
			updatePoints(lastTouched, -1);
			updatePoints(lastTouched, -1);
			updatePoints(lastTouched, -1);
		} else {
			updatePoints(lastTouched, 1);
		}
		lastTouched = null;
	}
}

function updatePoints(skillHandle, change) {
	var tree = skillHandle.parent().parent();
	var thisLevel = parseInt(skillHandle.parent().attr("data-level"));
	var invested = parseInt(skillHandle.parent().attr("data-invested"));
	var tierTotal = parseInt(skillHandle.parent().attr("data-total"));
	var treeTotal = parseInt(tree.find("span.totalPoints").text());
	var points = parseInt(skillHandle.attr("data-points"));
	var max = parseInt(skillHandle.attr("data-max"));
	var charLevel = parseInt($("span.charLevel").text());
	if(change > 0) {
		if (points < max && treeTotal >= 5 * thisLevel && charLevel < 72) {
			++points;
		}
	} else {
		if (points > 0) {
			var ok = true;
			tree.children("div.tier").each(function(index) {
				var level = parseInt($(this).attr("data-level"));
				var total = parseInt($(this).attr("data-total")) - (level == thisLevel ? 1 : 0);
				var invested = parseInt($(this).attr("data-invested")) - (level > thisLevel ? 1 : 0);
				ok &= (
					(level == thisLevel && total == 0 && treeTotal >= invested + total) ||
					(level != thisLevel && total == 0) ||
					(total > 0 && (level * 5 <= invested))
				);
			});
			if (ok) {
				--points;
			}
		}
	}
	skillHandle.attr("data-points", points);
	updateTree(tree);
	updateStats();
}

function updateTree(treeHandle) {
	var totalPoints = 0;
	$(treeHandle).find("div.tier").each(function(index) {
		$(this).attr("data-invested", totalPoints); //the PREVIOUS tier running total
		var tierLevel = parseInt($(this).attr("data-level"));
		var tierTotal = 0;
		$(this).children("div.skill").each(function(index) {
			var p = parseInt($(this).attr("data-points"));
			var m = parseInt($(this).attr("data-max"));
			totalPoints += p;
			tierTotal += p;
			$(this).children("div.points").html(
				p + "/" + m
			);
			$(this).children("div.points").css("visibility", (totalPoints < 5 * tierLevel) ? "hidden" : "visible");
			$(this).removeClass("partial full");
			if (p != 0) {
				$(this).addClass(p < m ? "partial" : "full");
			}
			$(this).find("em").each(function(index) {
				var mod = parseFloat($(this).attr("data-mod"));
				if (isNaN(mod)) mod = 0;
				var base = parseFloat($(this).attr("data-base"));
				var sum = Math.round((Math.max(p,1) * base + mod)*100)/100; //Math.round to eliminate goofy float errors
				var plus = ($(this).attr("data-base").substring(0,1) === "+" ? "+" : "");
				$(this).html((sum > 0 ? plus : (sum == 0 ? "" : "-")) + sum);
			});
		});
		$(this).attr("data-total", tierTotal);
	});
	$(treeHandle).find("span.totalPoints").html(totalPoints);
	$(treeHandle).parent().children(".color").height(Math.min(80 + totalPoints * 59.0 / 5 + (totalPoints > 25 ? 21 : 0), 396));
}

function updateStats() {
	var total = 0;
	$("span.totalPoints").each(function(index) {
		total += parseInt($(this).text());
	});
	$("span.charLevel").html(5+total);
	var descriptions = "";
	$("div.skill").each(function(index) {
		var p = parseInt($(this).attr("data-points"));
		if (p > 0) {
			descriptions += "<div class='skillText'>" + $(this).children("div.description").html().replace("<h2>","<strong>").replace("</h2>", " " + p + ":</strong><div class='descriptionText'>") + "</div></div>";
		}
	});
	$("div.descriptionContainer").html(descriptions);
	var url = window.location.href.split("#")[0] + "#" + getHash();
	$("a.permalink").attr("href",url);
	$("a.permalink").html(url);
	window.location.replace(url);
}

function loadHash(hash) {
	var h = hash.replace("#","");
	$("div.skill").each(function(index) {
		$(this).attr("data-points", Math.min(h.charAt(index),parseInt($(this).attr("data-max"))));
	});
	updateStats();
}

function getHash() {
	var hash = "";
	$("div.skill").each(function(index) {
		hash += $(this).attr("data-points");
	});
	return hash;
}

$(document).ready(function () {
	$('div.skill').mousedown(handleMousedown);
	$('div.skill').mouseup(handleMouseup);
	$("div.treewrapper").bind("contextmenu", function() { return false; });
	if (window.location.hash != "") {
		loadHash(window.location.hash);
	}

	$("div.tree").each(function(index) {
		updateTree($(this));
	});
	updateStats();
});