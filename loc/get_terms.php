<?php
    $locations = get_terms('local-music', array(
            'orderby' => 'name'
        )
    );
    echo json_encode($locations);
?>