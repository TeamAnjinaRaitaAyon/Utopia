$(document).ready(function() {
    $("#HospitalType").change(function() {
        const url = $(this).data("place-type-url");
        const hospitalType = $(this).val();
        
        $.ajax({
            url: url,
            data: { 'HospitalType': hospitalType },
            success: function(data) {
                $("#PlaceType").html('<option selected>Choose a place type</option>');
                data.place_types.forEach(function(place) {
                    $("#PlaceType").append(`<option value="${place.id}">${place.name}</option>`);
                });
            }
        });
    });

    $("#PlaceType").change(function() {
        const url = $(this).data("hospital-url");
        const placeType = $(this).val();
        
        $.ajax({
            url: url,
            data: { 'PlaceType': placeType },
            success: function(data) {
                $("#Hospital").html('<option selected>Choose a hospital</option>');
                data.hospitals.forEach(function(hospital) {
                    $("#Hospital").append(`<option value="${hospital.id}">${hospital.name}</option>`);
                });
            }
        });
    });

    $("#Hospital").change(function() {
        const url = $(this).data("issue-url");
        const hospital = $(this).val();
        
        $.ajax({
            url: url,
            data: { 'Hospital': hospital },
            success: function(data) {
                $("#HealthIssue").html('<option selected>Choose an issue</option>');
                data.issues.forEach(function(issue) {
                    $("#HealthIssue").append(`<option value="${issue.id}">${issue.name}</option>`);
                });
            }
        });
    });

    $("#HealthIssue").change(function() {
        const url = $(this).data("doctor-url");
        const issue = $(this).val();
        
        $.ajax({
            url: url,
            data: { 'HealthIssue': issue },
            success: function(data) {
                $("#Doctor").html('<option selected>Choose a doctor</option>');
                if (data.doctors.length > 0) {
                    data.doctors.forEach(function(doctor) {
                        $("#Doctor").append(`<option value="${doctor.id}">${doctor.name}</option>`);
                    });
                } else {
                    alert("Sorry, no doctors available. Please try another option.");
                }
            }
        });
    });
});
